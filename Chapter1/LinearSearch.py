# 순차 탐색(Linear Search) 알고리즘과 시간 복잡도 분석의 핵심요소

def LSearch(array, target):

    for i, arr in enumerate(array):
        if arr == target:
            return i
    return -1


def main():
    array = [3, 5, 2, 4, 9]
    idx = LSearch(array, 4)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f"타깃 저장 인덱스: {idx}")

    idx = LSearch(array, 7)
    if idx == -1:
        print("탐색 실패")
    else:
        print(f"타깃 저장 인덱스: {idx}")


if __name__ == "__main__":
    main()

