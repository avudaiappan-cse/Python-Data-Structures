from collections import deque

my_queue = deque()
my_queue.append(12)
my_queue.append(52)
my_queue.append(22)
print(my_queue)
my_queue.pop()
print(my_queue)
my_queue.popleft()
print(my_queue)



class Queue():
    def __init__(self):
        self.queue = list()
    def push(self,item):
        self.queue.append(item)
    def pop(self):
        if(len(self.queue)>0):
            del(self.queue[0])
        else:
            return None
    def __str__(self):
        return str(self.queue)
