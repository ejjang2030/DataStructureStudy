# 퀵 정렬(Quick Sort)


def QuickSort(arr):
    if len(arr) > 1:
        pivot = arr[len(arr) - 1]
        left, mid, right = [], [], []
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return QuickSort(left) + mid + QuickSort(right)
    else:
        return arr


def QuickSortMain():
    arr = [3, 2, 4, 1, 7, 6, 5]

    arr = QuickSort(arr)

    for i in range(len(arr)):
        print(arr[i], end=' ')

    print()


if __name__ == '__main__':
    QuickSortMain()
