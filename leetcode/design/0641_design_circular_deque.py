# Doubly Linked List / Circular Array.
class MyCircularDeque:
    def __init__(self, k):
        self.data = [0] * k
        self.capacity = k
        self.size = 0
        self.head = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.data[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.data[(self.head + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.data[self.head]

    def getRear(self):
        return -1 if self.isEmpty() else self.data[(self.head + self.size - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
