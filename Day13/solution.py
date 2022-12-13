from functools import cmp_to_key
from base import *
read_test_case()
fname = advent_fname()
print("Using", fname)



class Signal:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        r = Signal.compare(self.value, other.value)
        if r or r is None:
            return True
        return False

    def __repr__(self):
        return str(self.value)

    @staticmethod
    def compare(a, b):
        _al = isinstance(a, list)
        _bl = isinstance(b, list)
        if _al != _bl:
            return Signal.compare(a, [b]) if _al else Signal.compare([a], b)
        if _al and _bl:
            for ai, bi in zip_longest(a, b, fillvalue=None):
                if ai is None: # First list is shorter
                    return True
                
                if bi is None: # Second list is shorter
                    return False
                
                i = Signal.compare(ai, bi)

                if i is not None:
                    return i
            return None
        if a == b:
            return None
        return a < b


s2 = Signal([[2]])
s6 = Signal([[6]])

c2 = 1 # 1 for indexing
c6 = 2 # 1 for s2, 1 for stupid indexing

summa = 0
idx = 1

def handle_2_6(l):
    global c2, c6
    if l < s2:
        c2 += 1
        c6 += 1
    elif l < s6:
        c6 += 1

for e in rsplit('\n\n', '\n', fname=fname):
    l1, l2 = map(Signal, map(eval, e)) # Suckit, eval!

    # part 1
    if l1 < l2:
        summa += idx
    
    # part 2
    for x in (l1,l2):
        handle_2_6(x)
    
    idx += 1


print("Part 1:")
print(summa)

print("Part 2:")
print(c2*c6)
