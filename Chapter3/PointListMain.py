class Point:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def showPointPos(self):
        print(f"[{self.xpos}, {self.ypos}]")

    def comparePoint(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return 0
        elif self.xpos == other.xpos:
            return 1
        elif self.ypos == other.ypos:
            return 2
        else:
            return -1


def main():
    lst = list()
    p1 = Point(2, 1)
    lst.append(p1)
    p2 = Point(2, 2)
    lst.append(p2)
    p3 = Point(3, 1)
    lst.append(p3)
    p4 = Point(3, 2)
    lst.append(p4)

    # 저장된 데이터 출력
    print(f"현재 데이터의 수: {len(lst)}")

    if lst is not None:
        for p in lst:
            p.showPointPos()
    print()

    # xpos가 2인 모든 데이터 삭제
    compPos = Point(2, 0)

    if lst is not None:
        l = list()
        for i, p in enumerate(lst):
            if p.comparePoint(compPos) == 1:
                continue
            l.append(p)
        lst = l

    # 삭제 후 남은 데이터 전체 출력
    print(f"현재 데이터의 수: {len(lst)}")

    if lst is not None:
        for p in lst:
            p.showPointPos()
    print()


main()
