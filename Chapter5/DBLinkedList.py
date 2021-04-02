class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DBLinkedList:
    def __init__(self):
        self.head = None
        self.cur = None
        self.numOfData = 0
        self.pdata = None

    def ListInit(self):
        self.__init__()

    def LInsert(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        newNode.prev = None
        self.head = newNode

        self.numOfData += 1

    def LFirst(self):
        if self.head is None:
            return False

        self.cur = self.head
        self.pdata = self.cur.data

        return True

    def LNext(self):
        if self.cur.next is None:
            return False

        self.cur = self.cur.next
        self.pdata = self.cur.data

        return True

    def LPrevious(self):
        if self.cur.prev is None:
            return False

        self.cur = self.cur.prev
        self.pdata = self.cur.data

        return True

    def LCount(self):
        return self.numOfData


def DBLinkedListMain():
    # 양방향 연결 리스트의 생성 및 초기화
    lst = DBLinkedList()
    data = int()
    lst.ListInit()

    # 8개의 데이터 저장
    lst.LInsert(1)
    lst.LInsert(2)
    lst.LInsert(3)
    lst.LInsert(4)
    lst.LInsert(5)
    lst.LInsert(6)
    lst.LInsert(7)
    lst.LInsert(8)

    # 저장된 데이터의 조회
    if lst.LFirst():
        print(lst.pdata, end=' ')

        # 오른쪽 노드로 이동하며 데이터 조회
        while lst.LNext():
            print(lst.pdata, end=' ')

        # 왼쪽 노드로 이동하며 데이터 조회
        while lst.LPrevious():
            print(lst.pdata, end=' ')

        print()


if __name__ == '__main__':
    DBLinkedListMain()
