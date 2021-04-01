class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.cur = None
        self.before = None
        self.numOfData = int()
        self.comp = None

    def ListInit(self):
        self.head = Node(None)
        self.head.next = None
        self.comp = None
        self.numOfData = 0
