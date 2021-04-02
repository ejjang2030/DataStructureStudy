from BinaryTree2 import *
from Chapter6.ListBaseStack import *


def MakeExpTree(bt_main, exp):
    stack = ListStack()

    stack.StackInit()

    for c in exp:
        pnode = bt_main.MakeBTreeNode()

        if c.isdigit():
            pnode.SetData(int(c))
        else:
            bt_main.MakeRightSubTree(pnode, stack.SPop())
            bt_main.MakeLeftSubTree(pnode, stack.SPop())
            pnode.SetData(c)

        stack.SPush(pnode)

    return stack.SPop()


def EvaluateExpTree(bt_main, bt):
    if bt.GetLeftSubTree() is None and bt.GetRightSubTree() is None:
        return int(bt_main.GetData(bt))

    op1 = EvaluateExpTree(bt_main, bt.GetLeftSubTree())
    op2 = EvaluateExpTree(bt_main, bt.GetRightSubTree())
    print(f"op1 : {op1} / op2 : {op2}")

    if bt_main.GetData(bt) == "+":
        return int(op1) + int(op2)
    elif bt_main.GetData(bt) == "-":
        return int(op1) - int(op2)
    elif bt_main.GetData(bt) == "*":
        return int(op1) * int(op2)
    elif bt_main.GetData(bt) == "/":
        return int(op1) // int(op2)

    return 0


def ShowNodeData(data):
    if 0 <= int(data) <= 9:
        print(data, end=' ')
    else:
        print(data, end=' ')


def ShowPrefixTypeExp(bt_main, bt):
    bt_main.PreorderTraverse(bt)


def ShowInfixTypeExp(bt_main, bt):
    bt_main.InorderTraverse(bt)


def ShowPostfixTypeExp(bt_main, bt):
    bt_main.PostorderTraverse(bt)


def ExpressionTreeMain():
    exp = "12+7*"
    bt_main = BTreeNode()
    eTree = MakeExpTree(bt_main, exp)

    print("전위 표기법의 수식: ", end='')
    ShowPrefixTypeExp(bt_main, eTree)
    print()

    print("중위 표기법의 수식: ", end='')
    ShowInfixTypeExp(bt_main, eTree)
    print()

    print("후위 표기법의 수식: ", end='')
    ShowPostfixTypeExp(bt_main, eTree)
    print()

    print(f"연산의 결과: {EvaluateExpTree(bt_main, eTree)}")


if __name__ == '__main__':
    ExpressionTreeMain()
