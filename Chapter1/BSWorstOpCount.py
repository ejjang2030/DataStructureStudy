def BSearch(array, target):
    first = 0
    last = len(array) - 1
    opCount = 0  # 비교연산의 횟수를 기록

    while first <= last:
        mid = int((first + last) / 2)

        if target == array[mid]:
            return mid
        else:
            if target < array[mid]:
                last = mid - 1
            else:
                first = mid + 1

        opCount += 1  # 비교연산의 횟수 1 증가

    print(f"비교연산횟수: : {opCount}")  # 탐색 실패 시 연산횟수 출력
    return -1


def main():
    arr1 = [0 for _ in range(500)]
    arr2 = [0 for _ in range(5000)]
    arr3 = [0 for _ in range(50000)]

    # 리스트 arr1을 대상으로, 저장되지 않은 정수 1을 찾으라고 명령
    idx = BSearch(arr1, 1)
    if idx == -1:
        print("탐색 실패 ")
    else:
        print(f"타겟 저장 인덱스 : {idx}")

    # 리스트 arr2를 대상으로, 저장되지 않은 정수 2를 찾으라고 명령
    idx = BSearch(arr2, 2)
    if idx == -1:
        print("탐색 실패 ")
    else:
        print(f"타겟 저장 인덱스 : {idx}")

    # 리스트 arr3를 대상으로, 저장되지 않은 정수 3를 찾으라고 명령
    idx = BSearch(arr3, 3)
    if idx == -1:
        print("탐색 실패 ")
    else:
        print(f"타겟 저장 인덱스 : {idx}")


if __name__ == "__main__":
    main()
