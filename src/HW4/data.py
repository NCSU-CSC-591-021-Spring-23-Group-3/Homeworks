from row import ROW
from cols import COLS
from utils import *
from operator import itemgetter

class DATA:
    def __init__(self, src):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)

    def add(self, t):
        if self.cols:
            t = ROW(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=COLS(t)
    
    def stats(self, what, cols, nPlaces):
        def fun(_, col):
            if what == 'div':
                val = col.div()
            else:
                val = col.mid()
            return col.rnd(val, nPlaces),col.txt
        return kap(cols or self.cols.y, fun)
    
    def dist(self, row1, row2, cols = None):
        n,d = 0,0
        for col in cols or self.cols.x:
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**the['p']
        return (d/n)**(1/the['p'])

    def clone(self, init = {}):
        data = DATA([self.cols.names])
        _ = list(map(data.add, init))
        return data

    def around(self, row1, rows = None, cols = None):
        def function(row2):
            return {'row' : row2, 'dist' : self.dist(row1,row2,cols)} 
        return sorted(list(map(function, rows or self.rows)), key=itemgetter('dist'))

    def furthest(self, row1, rows = None, cols = None):
        t=self.around(row1,rows,cols)
        return t[len(t) - 1]