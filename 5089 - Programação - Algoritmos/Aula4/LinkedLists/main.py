"""
import LinkedList.node as n

node = n.Node(10)
node.next_node = n.Node(15)
node.next_node.next_node = n.Node()
node.next_node.next_node.next_node = n.Node(20)



temp = node
while temp is not None:
    print(temp.data)
    temp = temp.next_node

"""

from LinkedList.LinkedList import LinkedList


list1 = LinkedList()

list1.addNodeTail(10)
list1.addNodeTail(20)
list1.addNodeTail(30)
list1.addNodeHead(99)

list1.printList()


list1.find_node(30)

