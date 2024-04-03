
class Queue:

    def __init__(self, maxSize=-1, tipo=None):

        self.tipo = tipo

        self.maxSize = maxSize
        self.items = []

    def enqueue(self, item):

        if not self.isFull():
            if type(item) != list:
                self.__enqueue_val(item)
            else:
                self.__enqueue_list(item)
        else:
            print("Queue is full")

    def __enqueue_list(self, lista: list):
        for item in lista:
            self.__enqueue_val(item)

    def __enqueue_val(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self, pos=1):
        if self.size() < pos:
            return self.items[-1]
        if pos <= 0:
            return self.items[0]

        return self.items[pos-1]

    def size(self):
        return self.items.__len__()

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        if self.maxSize != -1:
            return self.size() >= self.maxSize
        return False

    def clear(self):
        self.items = []

    def remove(self, item, all= False):
        if all == False:
            self.items.remove(item)
        else:
            self.__remove_all(item)

    def __remove_all(self, item):
        while item in self.items:
            self.items.remove(item)

    def __str__(self):
        return str(self.items)

