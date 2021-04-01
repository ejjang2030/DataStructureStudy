class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    head = None
    cur = None

    while True:
        readData = int(input("자연수 입력 : "))
        if readData < 1:
            break

        # 노드의 추가과정
        newNode = Node(readData)
        if head is None:
            head = newNode
            cur = head
        else:
            cur.next = newNode
        cur = newNode

    print()

    # 입력 받은 데이터의 출력과정
    print("입력 받은 데이터의 전체출력! ")
    if head is None:
        print("저장된 자연수가 존재하지 않습니다.")
    else:
        cur = head
        print(cur.data, end=' ')
        while cur.next is not None:
            cur = cur.next
            print(cur.data, end=' ')

    print()
    print()

    if head is not None:
        delNode = head
        delNextNode = head.next

        print(f"{head.data}을(를) 삭제합니다.")
        del delNode

        while delNextNode:
            delNode = delNextNode
            delNextNode = delNextNode.next

            print(f"{delNode.data}을(를) 삭제합니다.")
            del delNode


main()

