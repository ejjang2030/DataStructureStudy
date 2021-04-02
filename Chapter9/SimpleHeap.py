class HeapElem:
    def __init__(self, pr, data):
        self.pr = pr
        self.data = data


class Heap:
    def __init__(self):
        self.heapArr = [HeapElem(int(), None)]

    def HeapInit(self):
        self.__init__()

    def HIsEmpty(self):
        if len(self.heapArr) == 1:
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
        if Heap.GetLChildIDX(idx) > len(self.heapArr) - 1:
            return 0
        elif Heap.GetLChildIDX(idx) == len(self.heapArr) - 1:
            return Heap.GetLChildIDX(idx)
        else:
            if self.heapArr[Heap.GetLChildIDX(idx)].pr > self.heapArr[Heap.GetRChildIDX(idx)].pr:
                return Heap.GetRChildIDX(idx)
            else:
                return Heap.GetLChildIDX(idx)

    # 힙에 데이터 저장
    def HInsert(self, data, priority):
        idx = len(self.heapArr)
        nelem = HeapElem(priority, data)
        self.heapArr.append(nelem)
        while idx != 1:
            if priority < self.heapArr[Heap.GetParentIDX(idx)].pr:
                self.heapArr[idx], self.heapArr[Heap.GetParentIDX(idx)] = self.heapArr[Heap.GetParentIDX(idx)], self.heapArr[idx]
                idx = Heap.GetParentIDX(idx)
            else:
                break

    def HDelete(self):
        retData = self.heapArr[1].data
        lastElem = self.heapArr[-1]

        parentIdx = 1
        childIdx = self.GetHiPriChildIDX(parentIdx)

        while childIdx == self.GetHiPriChildIDX(1):
            if lastElem.pr <= self.heapArr[childIdx].pr:
                break
            self.heapArr[parentIdx] = self.heapArr[childIdx]
            parentIdx = childIdx

        self.heapArr[parentIdx] = lastElem
        return retData


def SimpleHeapMain():
    heap = Heap()
    heap.HeapInit()  # 힙의 초기화

    heap.HInsert('A', 1)
    heap.HInsert('B', 2)
    heap.HInsert('C', 3)
    print(heap.HDelete())

    heap.HInsert('A', 1)
    heap.HInsert('B', 2)
    heap.HInsert('C', 3)
    print(heap.HDelete())

    while not heap.HIsEmpty():
        print(heap.HDelete())


if __name__ == '__main__':
    SimpleHeapMain()