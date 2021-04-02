import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def DequeInit(self):
        self.__init__()

    def DQIsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def DQAddFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.DQIsEmpty():
            self.tail = newNode
        else:
            self.head.prev = newNode

        newNode.prev = None
        self.head = newNode

    def DQAddLast(self, data):
        newNode = Node(data)
        newNode.prev = self.tail

        if self.DQIsEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode

        newNode.next = None
        self.tail = newNode

    def DQRemoveFirst(self):
        rnode = self.head

        if self.DQIsEmpty():
            print("Deque Memory Error!")
            sys.exit(-1)
        rdata = self.head.data

        self.head = self.head.next
        del rnode

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return rdata

    def DQRemoveLast(self):
        rnode = self.tail

        if self.DQIsEmpty():
            print("Deque Memory Error!")
            sys.exit(-1)
        rdata = self.tail.data

        self.tail = self.tail.prev
        del rnode

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return rdata

    def DQGetFirst(self):
        if self.DQIsEmpty():
            print("Deque Memory Error!")
            sys.exit(-1)

        return self.head.data

    def DQGetLast(self):
        if self.DQIsEmpty():
            print("Deque Memory Error!")
            sys.exit(-1)

        return self.tail.data


def DequeMain():
    # Deque의 생성 및 초기화
    deq = Deque()
    deq.DequeInit()

    # 데이터 넣기 1차
    deq.DQAddFirst(3)
    deq.DQAddFirst(2)
    deq.DQAddFirst(1)

    deq.DQAddLast(4)
    deq.DQAddLast(5)
    deq.DQAddLast(6)

    # 데이터 꺼내기 1차
    while not deq.DQIsEmpty():
        print(deq.DQRemoveFirst(), end=' ')

    print()

    # 데이터 넣기 2차
    deq.DQAddFirst(3)
    deq.DQAddFirst(2)
    deq.DQAddFirst(1)

    deq.DQAddLast(4)
    deq.DQAddLast(5)
    deq.DQAddLast(6)

    # 데이터 꺼내기 2차
    while not deq.DQIsEmpty():
        print(deq.DQRemoveLast(), end=' ')


if __name__ == "__main__":
    DequeMain()
