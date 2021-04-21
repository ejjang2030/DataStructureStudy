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

    @staticmethod
    def RemoveLeftSubTree(bt):
        delNode = None
        if bt is not None:
            delNode = bt.left
            bt.left = None
        return delNode

    @staticmethod
    def RemoveRightSubTree(bt):
        delNode = None
        if bt is not None:
            delNode = bt.right
            bt.right = None
        return delNode

    @staticmethod
    def ChangeLeftSubTree(main, sub):
        main.left = sub

    @staticmethod
    def ChangeRightSubTree(main, sub):
        main.right = sub