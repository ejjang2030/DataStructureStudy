from ListBaseStack import *


def EvalRPNExp(exp):
    stack = ListStack()
    stack.StackInit()

    for c in exp:
        if c.isdigit():
            stack.SPush(int(c) - 0)
        else:
            op2 = int(stack.SPop())
            op1 = int(stack.SPop())

            if c == "+":
                stack.SPush(op1 + op2)
            elif c == "-":
                stack.SPush(op1 - op2)
            elif c == "*":
                stack.SPush(op1 * op2)
            elif c == "/":
                stack.SPush(op1 // op2)

    return stack.SPop()


def PostCalculatorMain():
    postExp1 = "42*8+"
    postExp2 = "123+*4/"

    print(f"{postExp1} = {EvalRPNExp(postExp1)}")
    print(f"{postExp2} = {EvalRPNExp(postExp2)}")


if __name__ == "__main__":
    PostCalculatorMain()

