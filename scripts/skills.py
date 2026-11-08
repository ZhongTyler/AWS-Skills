#!/usr/bin/env python3
"""Select portable skills; preview by default, preserve host data and conflicting files."""
import argparse
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
import _runtime as runtime

ROOT=Path(__file__).absolute().parents[1]
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['list','install','upgrade','status','rollback'])
    parser.add_argument('--target',type=Path)
    parser.add_argument('--names',nargs='+',default=[])
    parser.add_argument('--platform',choices=['codex','codebuddy'],default='codex')
    parser.add_argument('--transaction')
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    # The shared transaction engine is vendored, so this package works without meta or the release repository.
    runtime.METADATA='.agent-skills/'+args.platform
    runtime.STATE=runtime.METADATA+'/state.json'
    runtime.SKILL_DIRECTORY='.agents/skills' if args.platform=='codex' else '.codebuddy/skills'
    try:
        base=runtime.load(ROOT/'catalog.json')
        # Platform destinations are fixed allowlisted roots, not arbitrary user paths.
        for name,item in base['components'].items():item['destination']=runtime.SKILL_DIRECTORY+'/'+name
        runtime.CATALOG_OVERRIDE=base
        if args.operation=='list':
            result=runtime.load(ROOT/'skills.json')
        else:
            if args.target is None:raise runtime.ContractError('--target required')
            target=args.target.absolute()
            if target==ROOT or target.is_relative_to(ROOT):raise runtime.ContractError('Use a separate host workspace')
            current=runtime.state(target)
            if args.operation=='install':
                if not args.names:raise runtime.ContractError('Select at least one --names entry; no automatic all-skills install')
                result=runtime.install(ROOT,target,'add' if current else 'init',args.names,args.apply)
            elif args.operation=='upgrade':result=runtime.install(ROOT,target,'upgrade',args.names,args.apply)
            elif args.operation=='rollback':
                if not args.transaction:raise runtime.ContractError('--transaction required')
                result=runtime.rollback(target,args.transaction,args.apply)
            else:
                result={'installed':current is not None,'platform':args.platform,'version':(current or {}).get('version'),'skills':(current or {}).get('components',{}),'modified':[p for p,v in (current or {}).get('files',{}).items() if runtime.digest(runtime.read(runtime.safe(target,p)))!=v['sha256']]}
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if result.get('conflicts'):return 2
        return 0
    except (runtime.ContractError,OSError,ValueError,KeyError) as e:
        print(json.dumps({'error':str(e)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
