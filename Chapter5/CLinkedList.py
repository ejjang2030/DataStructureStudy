class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CList:
    def __init__(self):
        self.tail = None
        self.cur = None
        self.before = None
        self.numOfData = 0
        self.pdata = None

    def ListInit(self):
        self.__init__()

    def LInsertFront(self, data):
        newNode = Node(data)

        if self.tail is None:
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode

        self.numOfData += 1

    def LInsert(self, data):
        newNode = Node(data)

        if self.tail is None:
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode

        self.numOfData += 1

    def LFirst(self):
        if self.tail is None:
            return False

        self.before = self.tail
        self.cur = self.tail.next

        self.pdata = self.cur.data
        return True

    def LNext(self):
        if self.tail is None:
            return False

        self.before = self.cur
        self.cur = self.cur.next

        self.pdata = self.cur.data
        return True

    def LRemove(self):
        rpos = self.cur
        rdata = rpos.data

        if rpos == self.tail:
            if self.tail == self.tail.next:
                self.tail = None
            else:
                self.tail = self.before

        self.before.next = self.cur.next
        self.cur = self.before

        del rpos
        self.numOfData -= 1
        return rdata

    def LCount(self):
        return self.numOfData


def CLinkedListMain():
    # 원형 연결 리스트의 생성 및 초기화
    lst = CList()
    data = int()
    nodeNum = int()
    lst.ListInit()

    # 리스트에 5개의 데이터를 저장
    lst.LInsert(3)
    lst.LInsert(4)
    lst.LInsert(5)
    lst.LInsertFront(2)
    lst.LInsertFront(1)

    # 리스트에 저장된 데이터를 연속 3회 출력
    if lst.LFirst():
        print(lst.pdata, end=' ')
        for i in range(lst.LCount() * 3 - 1):
            if lst.LNext():
                print(lst.pdata, end=' ')

    print()

    # 2의 배수를 찾아서 모두 삭제
    nodeNum = lst.LCount()

    if nodeNum != 0:
        lst.LFirst()
        if lst.pdata % 2 == 0:
            lst.LRemove()

        for i in range(nodeNum - 1):
            lst.LNext()
            if lst.pdata % 2 == 0:
                lst.LRemove()

    # 전체 데이터 1회 출력
    if lst.LFirst():
        print(lst.pdata, end=' ')

        for i in range(lst.LCount() - 1):
            if lst.LNext():
                print(lst.pdata, end=' ')


if __name__ == '__main__':
    CLinkedListMain()

