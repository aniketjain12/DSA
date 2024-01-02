class Stack(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
print(s.isEmpty())
print(s.size())
print(s.peek())
s.pop()
print(s.size())
print(s.peek())
s.pop()
print(s.size())
print(s.isEmpty())