from Chapter9.UsefulHeap import *
# 힙 정렬(Heap Sort)


def PriComp(n1, n2):
    return n2 - n1


def HeapSort(arr, pc):
    heap = Heap()
    heap.HeapInit(pc)

    # 정렬대상을 가지고 힙을 구성한다.
    for i in range(len(arr)):
        heap.HInsert(arr[i])

    # 순서대로 하나씩 꺼내서 정렬을 완성한다.
    for i in range(len(arr)):
        arr[i] = heap.HDelete()

    return arr


def HeapSortMain():
    arr = [3, 4, 2, 1]

    HeapSort(arr, PriComp)

    for i in range(4):
        print(arr[i], end=' ')

    print()


if __name__ == '__main__':
    HeapSortMain()


