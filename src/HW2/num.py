import math
from utils import rnd

class NUM:
    def __init__(self, at=None, txt=None):
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float("inf")
        self.hi = float("-inf")
        self.w = -1 if "-" in self.txt else 1



