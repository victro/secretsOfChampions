import mmap
with open('brackets.in', 'r') as infile:
    sequence = infile.readline().strip()
    resultArray = []
    while sequence:
        stack = []
        result = True
        for sym in sequence:
            if sym == '(' or sym == '[':
                stack.append(sym)
            else:
                if stack != []:
                    openTag = stack.pop()
                else:
                    result = False
                    break
                closeTag = sym
                if (openTag == '[' and closeTag != ']') or (openTag == '(' and closeTag != ')'):
                    result = False
                    break
        if stack != []:
            result = False
        if result == True:
            resultArray.append("YES")
        else:
            resultArray.append("NO")
        sequence = infile.readline().strip()
    infile.close()
with open('brackets.out', 'w') as outfile:
    outfile.write('\n'.join(resultArray))
    outfile.close()