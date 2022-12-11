from base import *
read_test_case()
fname = advent_fname()
print("Using", fname)

ms = [4, 14]

with open(fname) as f:
    v = f.read().strip()

_start = min(ms)
solutions = []
for i in range(_start, len(v)):
    # Add new element, remove old
    for j, m in enumerate(ms):
        running = set(v[i-m:i])
        if len(running) == m:
            ms.pop(j)
            solutions.append(i)
    if not ms:
        break

for i, e in enumerate(solutions, start=1):
    print("Part", i, e)
