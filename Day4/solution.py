from base import *
read_test_case()
fname = advent_fname()
print("Using", fname)

s1 = 0
s2 = 0
l = []


def subrange(a1, a2, b1, b2):
    if b1 > b2:
        return False
    if a1 > a2:
        return False
    if a1 <= b1 and b2 <= a2:
        return True
    if b1 <= a1 and a2 <= b2:
        return True
    return False


def overlap(a1, a2, b1, b2):
    if b1 > b2 or a1 > a2:
        return False
    if a1 <= b1 and b1 <= a2:
        return True
    if a1 <= b2 and b2 <= a2:
        return True
    if b1 <= a1 and a1 <= b2:
        return True
    if b1 <= a2 and a2 <= b2:
        return True
    return False


for e in rsplit('\n', ',', '-', int, fname=fname):
    print(e)
    r1, r2 = e
    a1, a2 = r1
    b1, b2 = r2
    if subrange(a1, a2, b1, b2):
        s1 += 1
        s2 += 1
    elif subrange(a1, b2, b1, a2):
        s2 += 1

print(s1)
print(s2)
print(l)
