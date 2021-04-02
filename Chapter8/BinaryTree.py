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


def BinaryTreeMain():
    bt = BTreeNode()
    bt1 = bt.MakeBTreeNode()  # 노드 bt1 생성
    bt2 = bt.MakeBTreeNode()  # 노드 bt2 생성
    bt3 = bt.MakeBTreeNode()  # 노드 bt3 생성
    bt4 = bt.MakeBTreeNode()  # 노드 bt4 생성

    bt1.SetData(1)  # bt1에 1 저장
    bt2.SetData(2)  # bt2에 2 저장
    bt3.SetData(3)  # bt3에 3 저장
    bt4.SetData(4)  # bt4에 4 저장

    bt.MakeLeftSubTree(bt1, bt2)  # bt2를 bt1의 왼쪽 자식 노드로
    bt.MakeRightSubTree(bt1, bt3)  # bt3를 bt1의 오른쪽 자식 노드로
    bt.MakeLeftSubTree(bt2, bt4)  # bt4를 bt2의 왼쪽 자식 노드로

    # bt1의 왼쪽 자식 노드의 데이터 출력
    print(bt.GetData(bt1.GetLeftSubTree()))

    # bt1의 왼쪽 자식 노드의 왼쪽 자식 노드의 데이터 출력
    print(bt.GetData(bt1.GetLeftSubTree().GetLeftSubTree()))


if __name__ == "__main__":
    BinaryTreeMain()
