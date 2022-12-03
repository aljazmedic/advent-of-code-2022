from base import *
fname = advent_fname()
print("Using", fname)

s1 = 0
s2 = 0
for e in rsplit('\n',' ', fname=fname):
    #print(e)
    a, b = e
    c1 = "ABC".index(a)
    c2 = "XYZ".index(b)

    # P1
    # c2 is our hand
    outcome = ((c2-c1+1) % 3)  # Mod difference by 3 to get the lose/draw/win
    s1 += outcome*3
    s1 += c2+1

    # P2
    # c2 is outcome
    # Mod difference by 3 to get the rock/paper/scissors
    our_hand = (c2-1 + c1) % 3
    s2 += c2*3
    s2 += our_hand+1

print(s1)
print(s2)
