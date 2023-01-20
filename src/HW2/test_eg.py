from utils import *
from num import NUM
from sym import SYM
from data import DATA

def test_the():
    print(the.__repr__())

def test_sym():
    sym = SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == rnd(sym.div())

def test_num():
    num = NUM()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    return 11/7 == num.mid() and 0.787 == rnd(num.div())

def no_of_chars_in_file(t):
    global n
    n += len(t)
    
def test_csv():
    csv(the['file'], no_of_chars_in_file)
    return n == 8*399

def test_data():
    data = DATA(the['file'])
    return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4

def test_stats():
    return True