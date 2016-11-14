import mmap
import sys
with open('snowmen.in', 'r') as infile:
    m = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)
    N = int(m.readline())
    sums = [0 for x in range(N + 1)]
    presums = [0 for x in range(N + 1)]
    clonedFrom = [0 for x in range(N + 1)]
    sumTotal = 0
    for i in range(N):
        inputs = m.readline().split()
        snowIndex = int(inputs[0])
        clonedFrom[i + 1] = snowIndex
        if inputs[1] == b'0':
            sums[i + 1] = presums[clonedFrom[i + 1]]
            presums[i + 1] = presums[clonedFrom[clonedFrom[i + 1]]]
            clonedFrom[i + 1] = clonedFrom[clonedFrom[snowIndex]]
            sumTotal += sums[i + 1]
        else:
            presums[i + 1] = sums[snowIndex]
            sums[i + 1] = sums[snowIndex] + int(inputs[1])
            sumTotal += sums[i + 1]
    m.close()
    infile.close()
with open('snowmen.out', 'w') as outfile:
    outfile.write(str(sumTotal))
    outfile.close()