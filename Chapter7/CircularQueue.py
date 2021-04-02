import sys


class CQueue:
    def __init__(self):
        self.front = int()
        self.rear = int()
        self.queArr = [None]

    def QueueInit(self):
        self.front = 0
        self.rear = 0

    def QIsEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def NextPosIdx(self, pos):
        if pos == len(self.queArr):
            return 0
        else:
            return pos + 1

    def Enqueue(self, data):
        if self.NextPosIdx(self.rear) == self.front:  # 큐가 꽉 찼다면
            print("Queue Memory Error!")
            sys.exit(-1)
        self.rear = self.NextPosIdx(self.rear)
        self.queArr.append(data)

    def Dequeue(self):
        if self.QIsEmpty():
            print("Queue Memory Error!")
            sys.exit(-1)

        self.front = self.NextPosIdx(self.front)
        return self.queArr[self.front]

    def QPeek(self):
        if self.QIsEmpty():
            print("Queue Memory Error!")
            sys.exit(-1)

        return self.queArr[self.NextPosIdx(self.front)]


def CircularQueueMain():
    # Queue의 생성 및 초기화
    q = CQueue()
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
    CircularQueueMain()
