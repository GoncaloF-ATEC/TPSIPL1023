
class Node():
    def __init__(self, data=None):
        self.next_node = None
        self.data = data

    def has_next(self) -> bool:
        return self.next_node is not None