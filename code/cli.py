from utils import the
import sys

help_msg = '''USAGE:   script.lua  [OPTIONS] [-g ACTION]
    OPTIONS:
    -d  --dump  on crash, dump stack = false
    -g  --go    start-up action      = data
    -h  --help  show help            = false
    -s  --seed  random number seed   = 937162211
    '''

def print_help_message():
    print(help_msg)

def parse_cli():
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == '--g' or args[i] ==  '--go':
            the['go'] = args[i+1]
        elif args[i] == '--s' or args[i] ==  '--seed':
            the['seed'] = int(args[i+1])
        elif args[i] == '--d' or args[i] ==  '--dump':
            the['dump'] = True
        elif args[i] == '--h' or args[i] ==  '--help':
            print_help_message()
        elif '-' in args[i]:
            raise Exception('INVALID OPTION: ' + args[i] + '\n' + help_msg)