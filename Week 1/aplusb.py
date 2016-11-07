import sys
import os
with open('aplusb.in', 'r') as input:
    variables = input.readline().split()
    a = int(variables[0])
    b = int(variables[1])
    result = a + b
with open('aplusb.out', 'w') as output:
    output.write(str(result))
    output.write('\n')