import sys, re

the = {
    'dump': False,
    'go': None,
    'seed': 937162211,
}

help = '''USAGE:   python main.py [OPTIONS] [-g ACTION]
    OPTIONS:
    -d  --dump  on crash, dump stack = false
    -g  --go    start-up action      = data
    -h  --help  show help            = false
    -s  --seed  random number seed   = 937162211
    '''

def settings(s):
    return re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",s)


def cli(options):
    args = sys.argv[1:]
    # for k, v in options:
    #     for n, x in enumerate(args):
    #         if x.startswith('-'+k[0]) or x.startswith('--'+k[0]):
    #             the[k] = True
    #         elif not x.__contains__('-'):
    #             the[args[n-1]]=x
    # print(args)
    # print(the)
    for i in range(len(args)):
        if args[i] == '--g' or args[i] ==  '--go':
            the['go'] = args[i+1]
        elif args[i] == '--s' or args[i] ==  '--seed':
            the['seed'] = int(args[i+1])
        elif args[i] == '--d' or args[i] ==  '--dump':
            the['dump'] = True
        elif args[i] == '--h' or args[i] ==  '--help':
            print(help)
        elif '-' in args[i]:
            raise Exception('INVALID OPTION: ' + args[i] + '\n' + help)