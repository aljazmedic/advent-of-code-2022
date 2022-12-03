from base import *
read_test_case()
fname = advent_fname()


V = " " + ascii_lowercase + ascii_uppercase + digits + punctuation
s1 = 0
l = []
for line in rsplit('\n', 0.5, fname=fname, group_n=None):
    print(line)
    v = reduce(set.intersection, map(set, line)).pop()
    s1 += V.index(v)

print(s1)

s1 = 0
l = []
for line in rsplit('\n', fname=fname, group_n=3):
    print(line)
    v = reduce(set.intersection, map(set, line)).pop()
    s1 += V.index(v)

print(s1)
