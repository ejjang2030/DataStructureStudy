class BTreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    @staticmethod
    def MakeBTreeNode():
        nd = BTreeNode()
        nd.left = None
        nd.right = None
        return nd

    @staticmethod
    def GetData(bt):
        return bt.data

    def SetData(self, data):
        self.data = data

    def GetLeftSubTree(self):
        return self.left

    def GetRightSubTree(self):
        return self.right

    @staticmethod
    def MakeLeftSubTree(main, sub):
        if main.left is not None:
            del main.left
        main.left = sub

    @staticmethod
    def MakeRightSubTree(main, sub):
        if main.right is not None:
            del main.right
        main.right = sub

    def PreorderTraverse(self, bt, action=print):
        if bt is None:
            return

        action(bt.data, end=' ')
        self.PreorderTraverse(bt.left, action)
        self.PreorderTraverse(bt.right, action)

    def InorderTraverse(self, bt, action=print):
        if bt is None:
            return

        self.InorderTraverse(bt.left, action)
        action(bt.data, end=' ')
        self.InorderTraverse(bt.right, action)

    def PostorderTraverse(self, bt, action=print):
        if bt is None:
            return

        self.PostorderTraverse(bt.left, action)
        self.PostorderTraverse(bt.right, action)
        action(bt.data, end=' ')


def ShowIntData(data, end):
    print(data, end=end)


def BinaryTreeMain2():
    bt = BTreeNode()
    bt1 = bt.MakeBTreeNode()
    bt2 = bt.MakeBTreeNode()
    bt3 = bt.MakeBTreeNode()
    bt4 = bt.MakeBTreeNode()
    bt5 = bt.MakeBTreeNode()
    bt6 = bt.MakeBTreeNode()

    bt1.SetData(1)
    bt2.SetData(2)
    bt3.SetData(3)
    bt4.SetData(4)
    bt5.SetData(5)
    bt6.SetData(6)

    bt.MakeLeftSubTree(bt1, bt2)
    bt.MakeRightSubTree(bt1, bt3)
    bt.MakeLeftSubTree(bt2, bt4)
    bt.MakeRightSubTree(bt2, bt5)
    bt.MakeRightSubTree(bt3, bt6)

    bt.PreorderTraverse(bt1, ShowIntData)
    print()
    bt.InorderTraverse(bt1, ShowIntData)
    print()
    bt.PostorderTraverse(bt1, ShowIntData)
    print()


if __name__ == '__main__':
    BinaryTreeMain2()
