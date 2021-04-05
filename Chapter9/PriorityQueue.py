from UsefulHeap import *


class PQueue(Heap):
    def PQueueInit(self, pc):
        Heap.HeapInit(self, pc)

    def PQIsEmpty(self):
        Heap.HIsEmpty(self)

    def PEnqueue(self, data):
        Heap.HInsert(self, data)

    def PDequeue(self):
        return Heap.HDelete(self)


def DataPriorityComp(ch1, ch2):
    return ord(ch2) - ord(ch1)


def PriorityQueueMain():
    pq = PQueue()
    pq.PQueueInit(DataPriorityComp)

    pq.PEnqueue('A')
    pq.PEnqueue('B')
    pq.PEnqueue('C')
    print(pq.PDequeue())

    pq.PEnqueue('A')
    pq.PEnqueue('B')
    pq.PEnqueue('C')
    print(pq.PDequeue())

    while not pq.PQIsEmpty():
        print(pq.PDequeue())


if __name__ == '__main__':
    PriorityQueueMain()
