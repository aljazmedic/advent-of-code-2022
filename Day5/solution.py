from base import *
import numpy as np
read_test_case()
fname = advent_fname()
print("Using", fname)

a, b = fread_split(fname, sep='\n\n', strip=False)

a = a.splitlines(True)
n = a[-1].count("   ") + 1
bins = [0]*n
for i in range(n):
    bins[i] = []
    for e in range(len(a)-2, -1, -1):
        v = a[e][1 + 4*i].strip()
        if v:
            bins[i].append(v)

r = re.compile(r'move (\d+) from (\d+) to (\d+)')
for line in b.strip().splitlines():
    m = r.match(line)
    n, a, b = map(int, m.groups())

    bins[a-1], take_off = bins[a-1][:-n], bins[a-1][-n:]
    # reverse for pt1
    #take_off = take_off[::-1]
    bins[b-1].extend(take_off)


print(bins)
s = ''.join([x[-1] for x in bins])
print(s)
