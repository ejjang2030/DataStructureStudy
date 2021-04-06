# 버블 정렬(Bubble Sort)

def BubbleSort(arr):
    temp = int()

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # 데이터의 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def BubbleSortMain():
    arr = [3, 2, 4, 1]

    arr = BubbleSort(arr)

    for i in range(4):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    BubbleSortMain()
