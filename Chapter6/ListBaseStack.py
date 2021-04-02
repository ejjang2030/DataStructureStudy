import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListStack:
    def __init__(self):
        self.head = None

    def StackInit(self):
        self.__init__()

    def SIsEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def SPush(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def SPop(self):
        if self.SIsEmpty():
            print("Stack Memory Error!")
            sys.exit(-1)

        rdata = self.head.data
        self.head = self.head.next

        return rdata

    def SPeek(self):
        if self.SIsEmpty():
            print("Stack Memory Error!")
            sys.exit(-1)

        return self.head.data


def ListBaseStackMain():
    # Stack의 생성 및 초기화
    stack = ListStack()
    stack.StackInit()

    # 데이터 넣기
    stack.SPush(1)
    stack.SPush(2)
    stack.SPush(3)
    stack.SPush(4)
    stack.SPush(5)

    # 데이터 꺼내기
    while not stack.SIsEmpty():
        print(stack.SPop(), end=' ')


if __name__ == '__main__':
    ListBaseStackMain()