from CircularQueue import *
import time
import random


def HamburgerSimMain():
    CUS_COME_TERM = 15

    CHE_BUR = 0
    BUL_BUR = 1
    DUB_BUR = 2

    CHE_TERM = 12
    BUL_TERM = 15
    DUB_TERM = 24

    makeProc = 0
    cheOrder = 0
    bulOrder = 0
    dubOrder = 0

    que = CQueue()
    que.QueueInit()

    random.seed(time.time())

    for sec in range(3600):
        if sec % CUS_COME_TERM == 0:
            if random.randint(0, 32767) % 3 == CHE_BUR:
                que.Enqueue(CHE_TERM)
                cheOrder += 1
            elif random.randint(0, 32767) % 3 == BUL_BUR:
                que.Enqueue(BUL_TERM)
                bulOrder += 1
            elif random.randint(0, 32767) % 3 == DUB_BUR:
                que.Enqueue(DUB_TERM)
                dubOrder += 1
        if makeProc <= 0 and not que.QIsEmpty():
            makeProc = que.Dequeue()
        makeProc -= 1

    print("Simulation Report! ")
    print(f" - Cheese burger: {cheOrder}")
    print(f" - Bulgogi burger: {bulOrder}")
    print(f" - Double burger: {dubOrder}")
    print(f" - Waiting room size: {len(que.queArr)}")


if __name__ == '__main__':
    HamburgerSimMain()