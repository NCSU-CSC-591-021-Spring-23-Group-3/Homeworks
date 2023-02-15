from utils import *
from num import NUM
from sym import SYM
from data import DATA

def test_the():
    print(the.__repr__())

def test_rand():
    Seed = 1
    t=[]
    for i in range(1,1000+1):
        t.append(rint(0,100,1))
    u=[]
    for i in range(1,1000+1):
        u.append(rint(0,100,1))
    for k,v in enumerate(t):
        assert(v==u[k])

def test_some():
    the['Max'] = 32
    num1 = NUM()
    for i in range(1,1000+1):
        num1.add(i)
    print(num1.has)

def test_num():
    num1, num2 = NUM(), NUM()
    global Seed
    Seed = the['seed']
    for i in range(1,10**3+1):
        num1.add(rand(0,1))
    Seed = the['seed']
    for i in range(1,10**3+1):
        num2.add(rand(0,1)**2)
    m1,m2 = rnd(num1.mid(),1), rnd(num2.mid(),1)
    d1,d2 = rnd(num1.div(),1), rnd(num2.div(),1)
    print(1, m1, d1)
    print(2, m2, d2) 
    return m1 > m2 and .5 == rnd(m1,1)

def test_sym():
    sym = SYM()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    print(sym.mid(), rnd(sym.div()))
    return 1.379 == rnd(sym.div())

def no_of_chars_in_file(t):
    global n
    n += len(t)

def test_csv():
    csv(the['file'], no_of_chars_in_file)
    return n == 3192

def test_data():
    data = DATA(the['file'])
    col=data.cols.x[1]
    print(col.lo,col.hi, col.mid(),col.div())
    print(data.stats('mid', data.cols.y, 2))

def test_clone():
    data1 = DATA(the['file'])
    data2 = data1.clone(data1.rows)
    print(data1.stats('mid', data1.cols.y, 2))
    print(data2.stats('mid', data2.cols.y, 2))

def test_cliffs():
    assert(False == cliffsDelta( [8,7,6,2,5,8,7,3],[8,7,6,2,5,8,7,3]))
    assert(True  == cliffsDelta( [8,7,6,2,5,8,7,3], [9,9,7,8,10,9,6])) 
    t1,t2=[],[]
    for i in range(1,1000+1):
        t1.append(rand(0,1))
    for i in range(1,1000+1):
        t2.append(rand(0,1)**.5)
    assert(False == cliffsDelta(t1,t1)) 
    assert(True  == cliffsDelta(t1,t2)) 
    diff,j=False,1.0
    while not diff:
        def function(x):
            return x*j
        t3=list(map(function, t1))
        diff=cliffsDelta(t1,t3)
        print(">",rnd(j),diff) 
        j=j*1.025

def test_dist():
    data = DATA(the['file'])
    num  = NUM()
    for row in data.rows:
        num.add(data.dist(row, data.rows[1]))
    print({'lo' : num.lo, 'hi' : num.hi, 'mid' : rnd(num.mid()), 'div' : rnd(num.div())})

def test_half():
    data = DATA(the['file'])
    left,right,A,B,mid,c = data.half() 
    print(len(left),len(right))
    l,r = data.clone(left), data.clone(right)
    print(A.cells,c)
    print(mid.cells) 
    print(B.cells)
    print("l",l.stats('mid', l.cols.y, 2))
    print("r",r.stats('mid', r.cols.y, 2))
# def test_copy():
#   t1 = {'a' : 1, 'b' : { 'c' : 2, 'd' : [3]}}
#   t2 = deepcopy(t1)
#   t2['b']['d'][0] = 10000
#   print('b4', t1, '\nafter', t2)

# def test_sym():
#     sym = SYM()
#     for x in ["a","a","a","a","b","b","c"]:
#         sym.add(x)
#     return "a" == sym.mid() and 1.379 == rnd(sym.div())

# def test_num():
#     num = NUM()
#     for x in [1,1,1,1,2,2,3]:
#         num.add(x)
#     return 11/7 == num.mid() and 0.787 == rnd(num.div())

# def test_repCols():
#     t = repCols(dofile(the['file'])['cols'], DATA)
#     _ = list(map(oo, t.cols.all))
#     _ = list(map(oo, t.rows))

# def test_synonyms():
#     data = DATA(the['file'])
#     show(repCols(dofile(the['file'])['cols'], DATA).cluster(),"mid",data.cols.all,1)

# def test_repRows():
#     t=dofile(the['file'])
#     rows = repRows(t, DATA, transpose(t['cols']))
#     _ = list(map(oo, rows.cols.all))
#     _ = list(map(oo, rows.rows))

# def test_prototypes():
#     t = dofile(the['file'])
#     rows = repRows(t, DATA, transpose(t['cols']))
#     show(rows.cluster(),"mid",rows.cols.all,1)

# def test_position():
#     t = dofile(the['file'])
#     rows = repRows(t, DATA, transpose(t['cols']))
#     rows.cluster()
#     repPlace(rows)

# def test_every():
#     repgrid(the['file'], DATA)