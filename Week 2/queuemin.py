import mmap
import sys
with open('queuemin.in', 'r') as infile:
    m = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)
    N = int(m.readline())
    oldStack = []
    newStack = []
    queueOut = []
    minnum = sys.maxsize
    oldStackSize = 0
    newStackSize = 0
    for i in range(N):
        inputs = m.readline().split()
        operation = inputs[0]
        if operation == b'-':
            if oldStack == []:
                minnum2 = sys.maxsize
                while newStack != []:
                    aux = newStack.pop()
                    newStackSize -= 1
                    minnum2 = min(minnum2, aux[0])
                    oldStack.append([aux[0], minnum2])
                    oldStackSize += 1
                minnum = sys.maxsize
            oldStack.pop()
            oldStackSize -= 1
            #print("POP")
            #print("old stack", oldStack)
            #print("new stack", newStack)
        elif operation == b'+':
            num = int(inputs[1])
            minnum = min(minnum, num)
            newStack.append([num, minnum])
            newStackSize += 1
            #print("PUSH", num)
            #print("old stack", oldStack)
            #print("new stack", newStack)
        else:
            #print("MIN QUERY")
            #print("old stack", oldStack)
            #print("new stack", newStack)

            if oldStack == []:
                queueOut.append(newStack[newStackSize - 1][1])
            elif newStack == []:
                queueOut.append(oldStack[oldStackSize - 1][1])
            else:
                queueOut.append(min(newStack[newStackSize - 1][1], oldStack[oldStackSize - 1][1]))
    m.close()
    infile.close()
with open('queuemin.out', 'w') as outfile:
    outfile.write('\n'.join(str(v) for v in queueOut))
    outfile.close()