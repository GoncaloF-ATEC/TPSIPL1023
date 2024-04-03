
class Node():
    def __init__(self, data=None):
        self.next_node = None
        self.data = data

    def has_next(self) -> bool:
        return self.next_node is not None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addNodeHead(self, data, nextNode: Node = None):
        newNode = Node(data)
        newNode.next_node = self.head
        self.head = newNode


    def addNodeTail(self, data, nextNode: Node = None):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
             self.__get_last_node().next_node = newNode



    def addAfterNode(self, data, new_data, nextNode: Node = None):
        pass


    def removeNode(self, data) -> Node:
        pass


    def isEmpty(self) -> bool:
        return self.head == None


    def find_node(self, data) -> Node:
        pass


    def __get_last_node(self) -> Node:
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        return temp


    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node
