

class Stack:
    def __init__(self, maxSize=-1, tipo=None):
        self.tipo = tipo
        self.maxSize = maxSize
        self.items = []

    def push(self, data):
        if self.tipo:
            if self.tipo == type(data):
                self.items.append(data)
            else:
                raise TypeError(f'Esta Setck so suporta valores de tipo {self.tipo.__name__}')
        else:
            self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items.__len__() == 0

    def clear(self):
        self.items = []

    def __str__(self):
        return str(self.items)