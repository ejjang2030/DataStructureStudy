class List:
    def __init__(self):
        self.arr = [int() for _ in range(100)]      # 리스트의 저장소인 배열
        self.numOfData = int()                      # 저장된 데이터의 수
        self.curPosition = int()                    # 데이터 참조위치를 기록
        self.data = int()

    def ListInit(self):
        self.numOfData = 0
        self.curPosition = -1

    def LInsert(self, data):
        if self.numOfData >= len(self.arr):
            print("저장이 불가능합니다.")
            return

        self.arr[self.numOfData] = data
        self.numOfData += 1

    def LFirst(self):
        if self.numOfData == 0:
            return False

        self.curPosition = 0
        self.data = self.arr[0]
        return True

    def LNext(self):
        if self.curPosition >= self.numOfData - 1:
            return False
        self.curPosition += 1
        self.data = self.arr[self.curPosition]
        return True

    def LRemove(self):
        rpos = self.curPosition
        num = self.numOfData
        rdata = self.arr[rpos]

        for i in range(rpos, num - 1):
            self.arr[i] = self.arr[i + 1]

        self.numOfData -= 1
        self.curPosition -= 1
        return rdata

    def LCount(self):
        return self.numOfData


def main():
    # List의 생성 및 초기화
    lst = List()
    data = 0
    lst.ListInit()

    # 5개의 데이터 저장
    lst.LInsert(11)
    lst.LInsert(11)
    lst.LInsert(22)
    lst.LInsert(22)
    lst.LInsert(33)

    # 저장된 데이터의 전체 출력
    print(f"현재 데이터의 수: {lst.LCount()}")

    if lst.LFirst():  # 첫 번째 데이터 조회
        print(lst.data, end=' ')
        while lst.LNext():  # 두 번째 이후의 데이터 조회
            print(lst.data, end=' ')
    print()

    #  숫자 22을 탐색하여 모두 삭제
    if lst.LFirst():
        if lst.data == 22:
            lst.LRemove()
        while lst.LNext():
            if lst.data == 22:
                lst.LRemove()

    # 삭제 후 남은 데이터 전체 출력
    print(f"현재 데이터 수: {lst.LCount()}")

    if lst.LFirst():
        print(lst.data, end=' ')
        while lst.LNext():
            print(lst.data, end=' ')
    print()


if __name__ == '__main__':
    main()