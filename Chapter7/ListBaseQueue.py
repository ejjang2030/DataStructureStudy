import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def QueueInit(self):
        self.__init__()

    def QIsEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def Enqueue(self, data):
        newNode = Node(data)

        if self.QIsEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def Dequeue(self):
        if self.QIsEmpty():
            print("Queue Memory Error!")
            sys.exit(-1)

        delNode = self.front
        retData = delNode.data
        self.front = self.front.next

        del delNode
        return retData

    def QPeek(self):
        if self.QIsEmpty():
            print("Queue Memory Error!")
            sys.exit(-1)

        return self.front.data


def ListBaseQueueMain():
    # Queue의 생성 및 초기화
    q = LQueue()
    q.QueueInit()

    # 데이터 넣기
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)
    q.Enqueue(5)

    # 데이터 꺼내기
    while not q.QIsEmpty():
        print(q.Dequeue(), end=' ')


if __name__ == "__main__":
    ListBaseQueueMain()