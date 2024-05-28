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


list1.addNodeTail(22)
list1.addNodeTail(23)
list1.addNodeTail(24)
list1.addNodeHead(12)

list1.printList()

list1.find_node(30)


def twoSum_ord(nums: list[int], target: int) -> list[int]:
    size = len(nums)

    pos = [0, size-1]
    sum = nums[0] + nums[size-1]

    while sum != target:

        if (nums[pos[0]] < 0 or nums[pos[1]] < 0) and sum > target:
            pos[0] += 1
        else:
            pos[1] -= 1
        sum = nums[pos[0]] + nums[pos[1]]

    return pos

def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for i in range(len(nums)):
        num = nums[i]
        if dict.get(num) is not None:
            return [dict.get(num), i]
        comp = target - num
        dict[comp] = i




print(twoSum([3,2,3], 6))
print( twoSum([3,2,4], 6))
print( twoSum([-1,-3,-4,-2,-5], -9))
print( twoSum([2,7,11,15], 9))




