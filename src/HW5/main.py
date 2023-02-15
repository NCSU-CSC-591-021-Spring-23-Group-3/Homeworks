#!/usr/bin/env python3

__author__ = "NCSU CSC 591 021 Spring 23 Group-3"
__version__ = "1.0.0"
__license__ = "MIT"

from utils import *
from test_hw5 import *

def main():
    y,n,saved = 0,0,deepcopy(the)
    for k,v in cli(settings(help)).items():
        the[k] = v
        saved[k] = v
    if the['help'] == True:
        print(help)
    else:
        for what, fun in egs.items():
            if the['go'] == 'all' or the['go'] == what:
                for k,v in saved.items():
                    the[k] = v
                Seed = the['seed']
                if egs[what]() == False:
                    n += 1
                    print('❌ fail:', what)
                else:
                    y += 1
                    print('✅ pass:', what)
    if y+n>0:
        print("🔆",{'pass' : y, 'fail' : n, 'success' :100*y/(y+n)//1})
    sys.exit(n)

if __name__ == '__main__':
    eg('the', 'show options', test_the)
    eg('rand', 'demo random number generation', test_rand)
    eg('some', 'demo of reservoir sampling', test_some)
    eg('nums', 'demo of NUM', test_num)
    eg('sym', 'demo SYMS', test_sym)
    eg('csv', 'reading csv files', test_csv)
    eg('data', 'showing DATA sets', test_data)
    eg('clone', 'replicate structure of a DATA', test_clone)
    eg('cliffs', 'start tests', test_cliffs)
    eg('dist', 'distance test', test_dist)
    eg('half', 'divide data in half', test_half)
    eg('tree', 'make snd show tree of clusters', test_tree)
    # eg('num', 'check nums', test_num)
    # eg('repcols', 'checking repcols', test_repCols)
    # eg('synonyms','checking repcols cluster', test_synonyms)
    # eg('reprows','checking reprows', test_repRows)
    # eg('prototypes','checking reprows cluster', test_prototypes)
    # eg('position','where\'s wally', test_position)
    # eg('every','the whole enchilada', test_every)
    main()