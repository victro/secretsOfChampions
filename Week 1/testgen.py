import sys
import os
import math
divisors = [0 for num in range((10 ** 7) + 1)]
def generateDivisors():
    for i in range(10 ** 7):
        counter = [0 for x in range(i)]
        num = i
        for j in range(2, i // 2):
            for k in range()
            if i % j == 0:
                counter[j] += 1
        print("divisor[" + str(i) + "]", divisors[i])
filein = open("chairs.in", "r")
fileout = open("chairs.out", "w")
inputs = filein.readline().split()
N = int(inputs[0])
generateDivisors()
#print("divisors array:", divisors)
result = 0
print(result)
fileout.write(str(result))
filein.close()
fileout.close()