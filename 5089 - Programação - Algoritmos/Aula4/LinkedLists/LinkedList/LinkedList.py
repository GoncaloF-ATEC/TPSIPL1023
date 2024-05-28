
class Node():
    def __init__(self, data=None):
        self.next_node = None
        self.data = data

    def has_next(self) -> bool:
        return self.next_node is not None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def addNodeHead(self, data):
        """
        Adiciona um node no head da lista
        :param data: Valor a ser adicionado a Lista
        :raise ValueError se data = None
        """


        if data is None:
            raise ValueError("Data cannot be None")


        newNode = Node(data)
        newNode.next_node = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode


    def addNodeTail(self, data: object) -> object:
        """

           Adiciona um node no tail da lista

           :param data: Valor a ser adicionado a Lista
           :raise ValueError se data = None

           """

        if data is None:
            raise ValueError("Data cannot be None")

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:

            self.tail.next_node = newNode
            self.tail = newNode

    def addAfterNode(self, data, new_data):
        if data is None:
            raise ValueError("Data cannot be None")
        if new_data is None:
            raise ValueError("Data cannot be None")


        node = self.find_node(data)
        new_node = Node(new_data, nextNode= node.next_node)
        node.next_node = new_node


    def removeNode(self, data) -> Node:
        pass





    def isEmpty(self) -> bool:
        return self.head == None


    def find_node(self, data) -> Node:
        """
        procura um node, se o node não existir devolve o tail (Ultimo valor da lista)
        :param data: valor a porcurar
        :return: node que contem o valor
        """
        temp = self.head
        while temp.next_node:
            if temp.data == data:
                return temp
            temp = temp.next_node
        return temp

    def conteins(self, data) -> (bool, Node):
        """

        devolve um tuplo que indica se um valor esta contido na lista.

        se existir devolve um tuplo comm (True, Node)
        se não existir devolve um tuplo comm (False, None)

        :param data:
        :return:
        """

        node = self.find_node(data)
        return (node is not None, node)


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

