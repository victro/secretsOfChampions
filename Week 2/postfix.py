import mmap
import sys
class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    #print(tokenList)
    for token in tokenList:
        if token in b"0123456789":
            operandStack.push(token[0] - 48) # ascii code for '0'
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == b"*":
        return op1 * op2
    elif op == b"+":
        return op1 + op2
    else:
        return op1 - op2


with open('postfix.in', 'r') as infile:
    m = mmap.mmap(infile.fileno(), 0, access = mmap.ACCESS_READ)
    postfixExpression = m.readline()
    #print("post fix expression", str(postfixExpression))
    result = postfixEval(postfixExpression)
    #print(result)
    m.close()
    infile.close()
with open('postfix.out', 'w') as outfile:
    #m = mmap.mmap(outfile.fileno(), 0, access = mmap.ACCESS_WRITE)
    outfile.write(str(result))
    #m.close()
    outfile.close()