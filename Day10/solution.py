from base import *
read_test_case()
fname = advent_fname()
print("Using", fname)

x = 1
l = []
s = 0
cycles = 0
for i, e in enumerate(rsplit('\n', fname=fname)):
    # print(e)
    if e.startswith("addx"):
        for _ in range(2):
            cycles += 1
            if cycles in (20, 60, 100, 140, 180, 220):
                print(e)
                s += x*cycles
                print("Cycle", cycles, "x", x, "s", s)  
        x += int(e[5:])
        
    elif e.startswith("noop"):
        for _ in range(1):
            cycles += 1
            if cycles in (20, 60, 100, 140, 180, 220):
                print(e)
                s += x*cycles
                print("Cycle", cycles, "x", x, "s", s) 
print(s)
print(l)
