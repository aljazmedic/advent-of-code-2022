from base import *
fname = advent_fname()
print("Using", fname)

s = 0
l = []
for e in rsplit('\n\n', '\n', fname=fname):
    print(e)
    v = (sum(map(int, e)))
    l.append(v)
    l.sort(reverse=True)
    l = l[:3]

print(l[0])
print(sum(l))
