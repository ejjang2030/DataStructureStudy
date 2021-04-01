# 이진 탐색(Binary Search) 알고리즘의 구현


def BSearch(array, target):
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = int((first + last) / 2)
        if target == array[mid]:
            return mid
        else:
            if target < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


def main():
    array = [1, 3, 5, 7, 9]
    idx = BSearch(array, 7)
    if idx == -1:
        print("탐색 실패 ")
    else:
        print(f"타깃 저장 인덱스 : {idx}")

    idx = BSearch(array, 4)
    if idx == -1:
        print("탐색 실패 ")
    else:
        print(f"타깃 저장 인덱스 : {idx}")


if __name__ == "__main__":
    main()

