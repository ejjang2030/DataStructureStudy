from BinaryTree import *


def InorderTravers(bt):
    if bt is None:
        return

    InorderTravers(bt.left)
    print(bt.data)
    InorderTravers(bt.right)


def BinaryTreeTraverseMain():
    bt = BTreeNode()
    bt1 = bt.MakeBTreeNode()
    bt2 = bt.MakeBTreeNode()
    bt3 = bt.MakeBTreeNode()
    bt4 = bt.MakeBTreeNode()

    bt1.SetData(1)
    bt2.SetData(2)
    bt3.SetData(3)
    bt4.SetData(4)

    bt.MakeLeftSubTree(bt1, bt2)
    bt.MakeRightSubTree(bt1, bt3)
    bt.MakeLeftSubTree(bt2, bt4)

    InorderTravers(bt1)


if __name__ == '__main__':
    BinaryTreeTraverseMain()
