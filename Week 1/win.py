import sys
import os
import math
filein = open("win.in", "r")
fileout = open("win.out", "w")
N = int(filein.readline())
vec = [int(num) for num in filein.readline().split()]
vec.sort()
res = N
limit = 18000
last = N
for i in range(len(vec)):
    last = N - i
    if sum(vec[0:last]) <= 18000:
        break
    else:
        res -= 1
fileout.write(str(res))
filein.close()
fileout.close()