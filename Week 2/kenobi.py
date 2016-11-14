import mmap
from collections import deque
def rotateOrNot(stack, mumCounter, tam):
    if tam % 2 == 0:
        if mumCounter % 2 != 0:
            middle = tam // 2
            stack.rotate(middle)
    else:
        middle = tam // 2
        mumCounter = mumCounter % tam
        if mumCounter % 2 == 0:
            degree = mumCounter // 2
        else:
            degree = middle + ((mumCounter + 1) // 2)
        if degree > 0 and tam % 2 == 0:
            degree -= 1
        if degree > 0:
            stack.rotate(degree)
with open('kenobi.in', 'r') as infile:
    m = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)
    N = int(m.readline())
    stack = deque([])
    counter = 0
    tam = 0
    mumCounter = 0
    degree = 0
    wholeInstructions = m.read().split(b'\n')
    for i in range(N):
        command = wholeInstructions[counter]
        counter += 1
        if command[0] == 97: #add
            if mumCounter > 0 and tam > 0:
                rotateOrNot(stack, mumCounter, tam)
                mumCounter = 0
            stack.append(int(command[4:])) # just adding the number to the stack
            tam += 1
        elif command[0] == 109: #mum!
            mumCounter += 1
        else: #take
            if mumCounter > 0 and tam > 0:
                rotateOrNot(stack, mumCounter, tam)
                mumCounter = 0
            stack.pop()
            tam -= 1
    if mumCounter > 0 and tam > 0:
            rotateOrNot(stack, mumCounter, tam)
            mumCounter = 0
    m.close()
    infile.close()
with open('kenobi.out', 'w') as outfile:
    outfile.write(str(tam))
    outfile.write('\n')
    outfile.write(' '.join(str(v) for v in stack))
    outfile.close()