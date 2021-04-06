# 삽입 정렬(Insertion Sort)

def InsertionSort(arr):
    for i in range(1, len(arr)):
        insData = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > insData:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = insData

    return arr


def InsertionSortMain():
    arr = [5, 3, 2, 4, 1]

    arr = InsertionSort(arr)

    for i in range(5):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    InsertionSortMain()
