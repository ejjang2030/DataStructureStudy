def ISearch(ar, first, last, target):
    if first > last:
        return -1  # -1의 반환은 탐색의 실패를 의미

    # 이진 탐색과의 차이점을 반영한 문장
    mid = int((target - ar[first]) / (ar[last] - ar[first]) * (last - first) + first)

    if ar[mid] == target:
        return mid  # 탐색된 타겟의 인덱스 값 반환
    elif target < ar[mid]:
        return ISearch(ar, first, mid - 1, target)
    else:
        return ISearch(ar, mid + 1, last, target)


def InterpolSearchMain():
    arr = [1, 3, 5, 7, 9]
    idx = int()

    idx = ISearch(arr, 0, len(arr) - 1, 7)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f"타겟 저장 인덱스: {idx}")

    idx = ISearch(arr, 0, len(arr) - 1, 10)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f'타겟 저장 인덱스: {idx}')


if __name__ == '__main__':
    InterpolSearchMain()
