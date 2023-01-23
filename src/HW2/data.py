from row import ROW
from cols import COLS
from utils import *;

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