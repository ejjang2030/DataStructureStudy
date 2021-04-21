from Chapter11.BinaryTree3 import *


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


def BSTRemove(pRoot, target):
    # 삭제 대상이 루트 노드인 경우를 별도로 고려해야 한다.
    pVRoot = BTreeNode.MakeBTreeNode()  # 가상 루트 노드
    pNode = pVRoot                      # parent node
    cNode = pRoot                       # current node
    dNode = None                        # delete node

    # 루트 노드를 pVRoot가 가리키는 노드의 오른쪽 자식 노드가 되게 한다.
    BTreeNode.ChangeRightSubTree(pVRoot, pRoot)

    # 삭제 대상인 노드를 탐색
    while (cNode is not None) and (BTreeNode.GetData(cNode) != target):
        pNode = cNode
        if target < BTreeNode.GetData(cNode):
            cNode = cNode.GetLeftSubTree()
        else:
            cNode = cNode.GetRightSubTree()

    if cNode is None:       # 삭제 대상이 존재하지 않는다면,
        return None

    dNode = cNode           # 삭제 대상을 dNode가 가리키게 한다.

    # 첫 번째 경우: 삭제 대상이 단말 노드인 경우
    if (dNode.GetLeftSubTree() is None) and (dNode.GetRightSubTree() is None):
        if pNode.GetLeftSubTree() == dNode:
            BTreeNode.RemoveLeftSubTree(pNode)
        else:
            BTreeNode.RemoveRightSubTree(pNode)
    # 두 번째 경우: 삭제 대상이 하나의 자식 노드를 갖는 경우
    elif (dNode.GetLeftSubTree() is None) or (dNode.GetRightSubTree() is None):
        dcNode = None       # 삭제 대상의 자식 노드 가리킴
        if dNode.GetLeftSubTree() is not None:
            dcNode = dNode.GetLeftSubTree()
        else:
            dcNode = dNode.GetRightSubTree()

        if pNode.GetLeftSubTree() == dNode:
            BTreeNode.ChangeLeftSubTree(pNode, dcNode)
        else:
            BTreeNode.ChangeRightSubTree(pNode, dcNode)
    # 세 번째 경우: 두 개의 자식 노드를 모두 갖는 경우
    else:
        mNode = dNode.GetRightSubTree()
        mpNode = dNode              # 대체 노드의 부모 노드 가리킴
        delData = int()

        # 삭제 대상의 대체 노드를 찾는다.
        while mNode.GetLeftSubTree() is not None:
            mpNode = mNode
            mNode = mNode.GetLeftSubTree()

        # 대체 노드에 저장된 값을 삭제할 노드에 대입한다.
        delData = BTreeNode.GetData(dNode)          # 대입 전 데이터 백업
        dNode.SetData(BTreeNode.GetData(mNode))     # 대입!

        # 대체 노드의 부모 노드와 자식 노드를 연결한다.
        if mpNode.GetLeftSubTree() == mNode:
            BTreeNode.ChangeLeftSubTree(mpNode, mNode.GetRightSubTree())
        else:
            BTreeNode.ChangeRightSubTree(mpNode, mNode.GetRightSubTree())

        dNode = mNode
        dNode.SetData(delData)      # 백업 데이터 복원

    # 삭제된 노드가 루트 노드인 경우에 대한 추가적인 처리
    if pVRoot.GetRightSubTree() != pRoot:
        pRoot = pVRoot.GetRightSubTree()            # 루트 노드의 변경을 반영

    del pVRoot      # 가상 루트 노드의 소멸
    del dNode    # 삭제 대상의 반환


def BSTShowAll(bst):
    bst.InorderTraverse(bst)       # 중위 순회


def BinarySearchTreeDelMain():

    bstRoot = None
    bstRoot = BSTInsert(bstRoot, 5)
    bstRoot = BSTInsert(bstRoot, 8)
    bstRoot = BSTInsert(bstRoot, 1)
    bstRoot = BSTInsert(bstRoot, 6)
    bstRoot = BSTInsert(bstRoot, 4)
    bstRoot = BSTInsert(bstRoot, 9)
    bstRoot = BSTInsert(bstRoot, 3)
    bstRoot = BSTInsert(bstRoot, 2)
    bstRoot = BSTInsert(bstRoot, 7)

    BSTShowAll(bstRoot)
    print()
    BSTRemove(bstRoot, 3)

    BSTShowAll(bstRoot)
    print()
    BSTRemove(bstRoot, 8)

    BSTShowAll(bstRoot)
    print()
    BSTRemove(bstRoot, 1)

    BSTShowAll(bstRoot)
    print()
    BSTRemove(bstRoot, 6)

    BSTShowAll(bstRoot)
    print()


if __name__ == '__main__':
    BinarySearchTreeDelMain()