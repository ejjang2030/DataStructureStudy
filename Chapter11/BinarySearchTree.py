from Chapter8.BinaryTree2 import *


def BSTMakeAndInit():
    pRoot = None
    return pRoot


def BSTGetNodeData(bst):
    return BTreeNode.GetData(bst)


def BSTInsert(pRoot, data):
    pNode = None  # Parent node
    cNode = pRoot  # Current node

    # 새로운 노드가(새 데이터가 담긴 노드가) 추가될 위치를 갖는다.
    while cNode is not None:
        if data == BTreeNode.GetData(cNode):
            return  # 데이터의(키의) 중복을 허용하지 않음
        pNode = cNode

        if BTreeNode.GetData(cNode) > data:
            cNode = cNode.GetLeftSubTree()
        else:
            cNode = cNode.GetRightSubTree()

    # pNode의 자식 노드로 추가할 새 노드의 생성
    nNode = BTreeNode.MakeBTreeNode()  # 새 노드의 생성
    nNode.SetData(data)  # 새 노드에 데이터 저장

    # pNode의 자식 노드로 새 노드를 추가
    if pNode is not None:  # 새 노드가 루트 노드가 아니라면,
        if data < BTreeNode.GetData(pNode):
            BTreeNode.MakeLeftSubTree(pNode, nNode)
        else:
            BTreeNode.MakeRightSubTree(pNode, nNode)
    else:  # 새 노드가 루트 노드라면,
        pRoot = nNode

    return pRoot


def BSTSearch(bst, target):
    cNode = bst

    while cNode is not None:
        cd = BTreeNode.GetData(cNode)

        if target == cd:
            return cNode
        elif target < cd:
            cNode = cNode.GetLeftSubTree()
        else:
            cNode = cNode.GetRightSubTree()

    return None


def BinarySearchTreeMain():

    bstRoot = None
    bstRoot = BSTInsert(bstRoot, 9)
    bstRoot = BSTInsert(bstRoot, 1)
    bstRoot = BSTInsert(bstRoot, 6)
    bstRoot = BSTInsert(bstRoot, 2)
    bstRoot = BSTInsert(bstRoot, 8)
    bstRoot = BSTInsert(bstRoot, 3)
    bstRoot = BSTInsert(bstRoot, 5)

    sNode = BSTSearch(bstRoot, 1)
    if sNode is None:
        print("탐색 실패 ")
    else:
        print(f"탐색에 성공한 키의 값 : {BSTGetNodeData(sNode)}")

    sNode = BSTSearch(bstRoot, 4)
    if sNode is None:
        print("탐색 실패 ")
    else:
        print(f"탐색에 성공한 키의 값 : {BSTGetNodeData(sNode)}")

    sNode = BSTSearch(bstRoot, 6)
    if sNode is None:
        print("탐색 실패 ")
    else:
        print(f"탐색에 성공한 키의 값 : {BSTGetNodeData(sNode)}")

    sNode = BSTSearch(bstRoot, 7)
    if sNode is None:
        print("탐색 실패 ")
    else:
        print(f"탐색에 성공한 키의 값 : {BSTGetNodeData(sNode)}")

    
if __name__ == '__main__':
    BinarySearchTreeMain()