# 04-2 단순 연결 리스트의 ADT와 구현
# 첫번째 리스트 : 연결 형태가 한쪽 방향으로 전개되고 시작과 끝이 분명히 존재하는 '단순 연결 리스트'
# * 정렬 기능이 추가된 연결 리스트의 ADT정의

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def WhoIsPrecede(d1, d2):
    if d1 < d2:
        return False  # d1이 정렬 순서상 앞선다.
    else:
        return True  # d2가 정렬 순서상 앞서거나 같다.


class LinkedList:
    def __init__(self):
        self.head = None
        self.cur = None
        self.before = None
        self.numOfData = int()
        self.comp = None
        self.pdata = None

    def ListInit(self):
        self.head = Node(None)
        self.head.next = None
        self.comp = None
        self.numOfData = 0

    def FInsert(self, data):
        newNode = Node(data)
        newNode.next = self.head.next
        self.head.next = newNode
        self.numOfData += 1

    def SInsert(self, data):
        newNode = Node(data)
        pred = self.head

        while pred.next is not None and WhoIsPrecede(data, pred.next.data):
            pred = pred.next

        newNode.next = pred.next
        pred.next = newNode
        self.numOfData += 1

    def LInsert(self, data):
        if self.comp is None:
            self.FInsert(data)
        else:
            self.SInsert(data)

    def LFirst(self):
        if self.head.next is None:
            return False

        self.before = self.head
        self.cur = self.head.next

        self.pdata = self.cur.data
        return True

    def LNext(self):
        if self.cur.next is None:
            return False

        self.before = self.cur
        self.cur = self.cur.next

        self.pdata = self.cur.data
        return True

    def LRemove(self):
        rpos = self.cur
        rdata = rpos.data

        self.before.next = self.cur.next
        self.cur = self.before

        del rpos
        self.numOfData -= 1
        return rdata

    def LCount(self):
        return self.numOfData

    # 정렬 기준을 설정
    def setSortRule(self):
        self.comp = WhoIsPrecede


def DLinkedListMain():
    print("DLinkedListMain()")
    # 리스트의 생성 및 초기화
    lst = LinkedList()
    data = int()
    lst.ListInit()

    # 5개의 데이터 저장
    lst.LInsert(11)
    lst.LInsert(11)
    lst.LInsert(22)
    lst.LInsert(22)
    lst.LInsert(33)

    # 저장된 데이터의 전체 출력
    print(f"현재 데이터의 수: {lst.LCount()}")

    if lst.LFirst():
        print(lst.pdata, end=' ')

        while lst.LNext():
            print(lst.pdata, end=' ')

    print()
    print()

    # 숫자 22을 검색하여 모두 삭제
    if lst.LFirst():
        if lst.pdata == 22:
            lst.LRemove()

        while lst.LNext():
            if lst.pdata == 22:
                lst.LRemove()

    # 삭제 후 남아있는 데이터 전체 출력
    print(f"현재 데이터의 수: {lst.LCount()}")

    if lst.LFirst():
        print(lst.pdata, end=' ')

        while lst.LNext():
            print(lst.pdata, end=' ')

    print()
    print()


def DLinkedListSortMain():
    print("DLinkedListSortMain()")

    # 리스트의 생성 및 초기화
    lst = LinkedList()
    data = int()
    lst.ListInit()

    lst.setSortRule()  # 정렬의 기준을 등록한다.

    # 5개의 데이터 저장
    lst.LInsert(11)
    lst.LInsert(11)
    lst.LInsert(22)
    lst.LInsert(22)
    lst.LInsert(33)

    # 저장된 데이터의 전체 출력
    print(f"현재 데이터의 수: {lst.LCount()}")

    if lst.LFirst():
        print(lst.pdata, end=' ')

        while lst.LNext():
            print(lst.pdata, end=' ')

    print()
    print()

    # 숫자 22을 검색하여 모두 삭제
    if lst.LFirst():
        if lst.pdata == 22:
            lst.LRemove()

        while lst.LNext():
            if lst.pdata == 22:
                lst.LRemove()

    # 삭제 후 남아있는 데이터 전체 출력
    print(f"현재 데이터의 수: {lst.LCount()}")

    if lst.LFirst():
        print(lst.pdata, end=' ')

        while lst.LNext():
            print(lst.pdata, end=' ')

    print()
    print()


if __name__ == '__main__':
    DLinkedListMain()
    DLinkedListSortMain()
