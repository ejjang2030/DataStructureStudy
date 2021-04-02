import sys


class ArrayStack:
    def __init__(self):
        self.stackArr = list()

    def SIsEmpty(self):
        if len(self.stackArr) == 0:
            return True
        else:
            return False

    def SPush(self, data):
        self.stackArr.append(data)

    def SPop(self):
        if self.SIsEmpty():
            print("Stack Memory Error!")
            sys.exit(-1)

        return self.stackArr.pop()

    def SPeek(self):
        if self.SIsEmpty():
            print("Stack Memory Error!")
            sys.exit(-1)

        return self.stackArr[-1]


def ArrayBaseStackMain():
    # Stack의 생성 및 초기화
    stack = ArrayStack()

    # 데이터 넣기
    stack.SPush(1)
    stack.SPush(2)
    stack.SPush(3)
    stack.SPush(4)
    stack.SPush(5)

    # 데이터 꺼내기
    while not stack.SIsEmpty():
        print(stack.SPop(), end=' ')


if __name__ == '__main__':
    ArrayBaseStackMain()
