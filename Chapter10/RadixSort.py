from Chapter7.ListBaseQueue import *


def RadixSort(arr, maxLen):
    # 매개변수 maxLen에는 정렬대상 중 가장 긴 데이터의 길이 정보가 전달
    buckets = []
    divfac = 1

    # 총 10개의 버킷 초기화
    for bi in range(10):
        buckets.append(LQueue())

    # 가장 긴 데이터의 길이만큼 반복
    for pos in range(maxLen):
        # 정렬대상의 수만큼 반복
        for di in range(len(arr)):
            # N번째 자리의 숫자 추출
            radix = int((arr[di] // divfac) % 10)

            # 추출한 숫자를 근거로 버킷에 데이터 저장
            buckets[radix].Enqueue(arr[di])

        # 버킷 수만큼 반복
        di = 0
        for bi in range(10):
            # 버킷에 저장된 것 순서대록 다 꺼내서 다시 arr에 저장
            while not buckets[bi].QIsEmpty():
                arr[di] = buckets[bi].Dequeue()
                di += 1

        # N번째 자리의 숫자 추출을 위한 피제수의 증가
        divfac *= 10

    return arr


def RadixSortMain():
    arr = [13, 212, 14, 7141, 10987, 6, 15]

    arr = RadixSort(arr, 5)

    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    RadixSortMain()
