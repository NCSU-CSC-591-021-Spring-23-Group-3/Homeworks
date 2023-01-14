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

egs = {}

Seed=937162211

def settings(s):
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",s))

def cli(options):
    args = sys.argv[1:]
    for k, v in options.items():
        for n, x in enumerate(args):
            if x == '-'+k[0] or x == '--'+k:
                if v == 'false':
                    options[k] = True
                elif v == 'true':
                    options[k] = False
                elif args[n+1].isdigit():
                    options[k] = int(args[n+1])
                elif '.' in args[n+1] and args[n+1].replace('.','').isdigit():
                    options[k] = float(args[n+1])
                else:
                    options[k] = args[n+1]  
    return options

def eg(key, str, fun):
    egs[key] = fun
    global help
    help = help + '  -g '+ key + '\t' + str + '\n'