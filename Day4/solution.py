from base import *
read_test_case()
fname = advent_fname()
print("Using", fname)

s1 = 0
s2 = 0
l = []


def subrange(a1, a2, b1, b2):
    if a1 <= b1 and b2 <= a2:
        return True
    if b1 <= a1 and a2 <= b2:
        return True
    return False


def disjoint(a1, a2, b1, b2):
    return a2 < b1 or b2 < a1


for e in rsplit('\n', ',', '-', int, fname=fname):
    print(e)
    r1, r2 = e
    a1, a2 = r1
    b1, b2 = r2
    if subrange(a1, a2, b1, b2):
        s1 += 1
    if not disjoint(a1, a2, b1, b2):
        s2 += 1

print(s1)
print(s2)
print(l)
