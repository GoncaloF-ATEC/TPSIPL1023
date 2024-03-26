import Queue as q


my_queue = q.Queue()

print(my_queue)
my_queue.enqueue(1)
print(my_queue)

my_queue.enqueue(2)
print(my_queue)

my_queue.enqueue(3)
print(my_queue)

my_queue.dequeue()
print(my_queue)

my_queue.dequeue()
my_queue.dequeue()

print(my_queue)

my_queue.dequeue()

my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)

print(my_queue.peek())
print(my_queue.peek(-1))

my_queue.clear()

print(my_queue)

my_queue.enqueue([1,2,3])
my_queue.enqueue(4)
print(my_queue.size())

my_queue.clear()

l = [1,2,3, 1]

my_queue.enqueue(l)

print(my_queue)

my_queue.remove(1, all= True)

print(my_queue)