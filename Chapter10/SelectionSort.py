# 선택 정렬(Selection Sort)

def SelectionSort(arr):
    maxIdx = int()

    for i in range(len(arr) - 1):
        maxIdx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[maxIdx]:
                maxIdx = j

        arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

    return arr


def SelectionSortMain():
    arr = [3, 4, 2, 1]

    arr = SelectionSort(arr)

    for i in range(4):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    SelectionSortMain()
