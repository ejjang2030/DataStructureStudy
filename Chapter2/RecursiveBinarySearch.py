def BSearchRecur(ar, first, last, target):
    if first > last:
        return -1                   # -1의 반환은 탐색의 실패를 의미
    mid = int((first + last) / 2)   # 탐색대상의 중앙을 찾는다.

    if ar[mid] == target:
        return mid                  # 탐색된 타겟의 인덱스 값 반환
    elif target < ar[mid]:
        return BSearchRecur(ar, first, mid - 1, target)
    else:
        return BSearchRecur(ar, mid + 1, last, target)


def main():
    arr = [1, 3, 5, 7, 9]

    idx = BSearchRecur(arr, 0, len(arr) - 1, 7)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f"타겟 저장 인덱스 : {idx}")

    idx = BSearchRecur(arr, 0, len(arr) - 1, 4)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f"타겟 저장 인덱스 : {idx}")


if __name__ == "__main__":
    main()
