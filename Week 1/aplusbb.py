import sys
import os
filein = open("aplusbb.in", "r")
fileout = open("aplusbb.out", "w")
inputs = filein.readline().split()
a = int(inputs[0])
b = int(inputs[1])
fileout.write(str(a + b**2))
filein.close()
fileout.close()