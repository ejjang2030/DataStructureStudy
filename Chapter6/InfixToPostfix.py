from ListBaseStack import *


def getOpPrec(op):
    if op == '*' or op == '/':
        return 5
    elif op == '+' or op == '-':
        return 3
    elif op == '(':
        return 1
    return -1


def whoPrecOp(op1, op2):
    op1Prec = getOpPrec(op1)
    op2Prec = getOpPrec(op2)

    if op1Prec > op2Prec:
        return 1
    elif op1Prec < op2Prec:
        return -1
    else:
        return 0


def convToRPNExp(exp):
    stack = ListStack()
    convExp = list()

    stack.StackInit()

    for c in exp:
        if c.isdigit():
            convExp.append(c)
        else:
            if c == "(":
                stack.SPush(c)

            elif c == ")":
                while True:
                    popOp = stack.SPop()
                    if popOp == "(":
                        break
                    convExp.append(popOp)

            elif c == "+" or c == "-" or c == "*" or c == "/":
                while (not stack.SIsEmpty()) and whoPrecOp(stack.SPeek(), c) >= 0:
                    convExp.append(stack.SPop())
                stack.SPush(c)

    while not stack.SIsEmpty():
        convExp.append(stack.SPop())

    exp = ''.join(convExp)
    del convExp
    return exp


def InfixToPostfixMain():
    exp1 = "1+2*3"
    exp2 = "(1+2)*3"
    exp3 = "((1-2)+3)*(5-2)"

    exp1 = convToRPNExp(exp1)
    exp2 = convToRPNExp(exp2)
    exp3 = convToRPNExp(exp3)

    print(exp1)
    print(exp2)
    print(exp3)


if __name__ == "__main__":
    InfixToPostfixMain()
