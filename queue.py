class Queue(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self,item):
    self.items.insert(0,item)

  def dequeue(self):
    self.items.pop()

  def size(self):
    return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue('two')
print(q.size())
print(q.isEmpty())

#a = q.dequeue()
print(q.dequeue())
print('\n')
print(q.size())
print(q.isEmpty())
print('\n')
b = q.dequeue()
print(b)
print(q.size())
print(q.isEmpty())


    