import sys
import os
filein = open("chairs.in", "r")
fileout = open("chairs.out", "w")
inputs = filein.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])
result = (a / 2) + (b / 2) + (c / 2)
result = result / 3
result = '{0:.10f}'.format(result)
print(result)
fileout.write(str(result))
filein.close()
fileout.close()