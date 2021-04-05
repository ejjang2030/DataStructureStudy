class Heap:
    def __init__(self):
        self.comp = None
        self.numOfData = int()
        self.heapArr = [None]

    def HeapInit(self, pc):  # pc : PriorityComp
        self.numOfData = 0
        self.comp = pc

    def HIsEmpty(self):
        if self.numOfData == 0:
            return True
        else:
            return False

    @staticmethod
    def GetParentIDX(idx):
        return int(idx // 2)

    @staticmethod
    def GetLChildIDX(idx):
        return idx * 2

    @staticmethod
    def GetRChildIDX(idx):
        return Heap.GetLChildIDX(idx) + 1

    def GetHiPriChildIDX(self, idx):
        if Heap.GetLChildIDX(idx) > self.numOfData:
            return 0
        elif Heap.GetLChildIDX(idx) == self.numOfData:
            return Heap.GetLChildIDX(idx)
        else:
            # if self.heapArr[Heap.GetLChildIDX(idx)].pr > self.heapArr[GetRChildIDX(idx)].pr:
            if self.comp(self.heapArr[Heap.GetLChildIDX(idx)], self.heapArr[Heap.GetRChildIDX(idx)]) < 0:
                return Heap.GetRChildIDX(idx)
            else:
                return Heap.GetLChildIDX(idx)

    def HInsert(self, data):
        idx = self.numOfData + 1
        self.heapArr.append(data)
        while idx != 1:
            # if pr < self.heapArr[Heap.GetParentIDX(idx)].pr:
            if self.comp(data, self.heapArr[Heap.GetParentIDX(idx)]) > 0:
                self.heapArr[idx], self.heapArr[Heap.GetParentIDX(idx)] = self.heapArr[Heap.GetParentIDX(idx)], self.heapArr[idx]
                idx = Heap.GetParentIDX(idx)
            else:
                break

        self.numOfData += 1

    def HDelete(self):
        retData = self.heapArr[1]
        lastElem = self.heapArr[self.numOfData]

        parentIdx = 1
        childIdx = self.GetHiPriChildIDX(parentIdx)

        while childIdx > 0:
            # if lastElem.pr <= self.heapArr[childIdx].pr:
            if self.comp(lastElem, self.heapArr[childIdx]) >= 0:
                break
            self.heapArr[parentIdx] = self.heapArr[childIdx]
            parentIdx = childIdx
            childIdx = self.GetHiPriChildIDX(parentIdx)

        self.heapArr[parentIdx] = lastElem
        self.numOfData -= 1
        return retData


def DataPriorityComp(ch1, ch2):  # 우선순위 비교함수
    return ord(ch2) - ord(ch1)


def UsefulHeapMain():
    heap = Heap()
    heap.HeapInit(DataPriorityComp)  # 우선순위 비교함수 등록

    heap.HInsert('A')
    heap.HInsert('B')
    heap.HInsert('C')
    print(heap.HDelete())

    heap.HInsert('A')
    heap.HInsert('B')
    heap.HInsert('C')
    print(heap.HDelete())

    while not heap.HIsEmpty():
        print(heap.HDelete())


if __name__ == '__main__':
    UsefulHeapMain()


