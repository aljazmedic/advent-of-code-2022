from base import *
import numpy as np
read_test_case()
fname = advent_fname()
print("Using", fname)


def f(x):
    return ord(x)-ord('a')


for e in rsplit('\n', fname=fname):
    h.append(list(map(f, e)))

h = np.array(h)

start = np.argwhere(h == f('S'))[0]
end = np.argwhere(h == f('E'))[0]

h[tuple(start)] = f('a')
h[tuple(end)] = f('z')


def bfs(start, end):
    dists = {}
    q = start
    for start in q:
        dists[tuple(start)] = 0
    while len(q) > 0:
        p = q.pop(0)
        # print(c)
        pt = tuple(p)
        if (p == end).all():
            return dists[pt]
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n = p+d
            nt = tuple(n)
            # check out of bounds
            if (n < 0).any() or (n >= h.shape).any():
                continue
            if nt in dists:
                continue
            if (h[nt]-h[pt]) <= 1:
                dists[nt] = dists[pt]+1
                q.append(n)
    return None


# Part 1
d = bfs([start], end)
print("Part 1:", d)

# Part 2
all_as = list(np.argwhere(h == f('a')))
d = bfs(all_as, end)
print("Part 2:", d)
