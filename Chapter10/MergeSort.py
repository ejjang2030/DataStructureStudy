# 병합 정렬(Merge Sort)


def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    # 중간 지점을 계산한다.
    mid = len(arr) // 2

    # 둘로 나눠서 각각을 정렬한다.
    arr_left = arr[:mid]
    arr_right = arr[mid:]
    arr_left = MergeSort(arr_left)
    arr_right = MergeSort(arr_right)

    # 정렬된 두 배열을 병합한다.
    return MergeTwoArea(arr_left, arr_right)


def MergeTwoArea(arr_left, arr_right):
    sortArr = list()
    fIdx, rIdx = 0, 0
    while fIdx < len(arr_left) and rIdx < len(arr_right):
        if arr_left[fIdx] <= arr_right[rIdx]:
            sortArr.append(arr_left[fIdx])
            fIdx += 1
        else:
            sortArr.append(arr_right[rIdx])
            rIdx += 1

    while fIdx < len(arr_left):
        sortArr.append(arr_left[fIdx])
        fIdx += 1

    while rIdx < len(arr_right):
        sortArr.append(arr_right[rIdx])
        rIdx += 1

    return sortArr


def MergeSortMain():
    arr = [3, 2, 4, 1, 7, 6, 5]

    # 배열 arr의 전체 영역 정렬
    arr = MergeSort(arr)

    for i in range(7):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    MergeSortMain()
