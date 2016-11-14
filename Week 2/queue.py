import mmap
with open('queue.in', 'r') as infile:
    N = int(infile.readline())
    queueOut = []
    queue = []
    counter = 0
    for i in range(N):
        inputs = infile.readline().split()
        operation = inputs[0]
        if operation == '-':
            queueOut.append(queue[counter])
            queue[0] = -1
            counter += 1
        else:
            queue.append(inputs[1])
    infile.close()
with open('queue.out', 'w') as outfile:
    outfile.write('\n'.join(queueOut))
    outfile.close()