import mmap
import math
with open('stacks.in', 'r') as infile:
    m = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)
    N = int(m.readline())
    maxStack = 1
    elems = [int(num) for num in m.readline().split()]
    counterOfZeros = 0
    counterOfNums = 0
    flag = False
    if elems[0] == 0:
       elems[0] = 1
    for i in range(N):
        if i > 0 and elems[i] > 0 and elems[i - 1] == 0:
            flag = True
        if flag == True:
            maxStack = max(maxStack, math.ceil(counterOfZeros / counterOfNums) + 1)
            flag = False
        if elems[i] > 0:
            counterOfNums += 1
        else:
            counterOfZeros += 1
        if i == N - 1:
            maxStack = max(maxStack, math.ceil(counterOfZeros / counterOfNums) + 1)
    infile.close()
with open('stacks.out', 'w') as outfile:
    outfile.write(str(maxStack))
    outfile.close()