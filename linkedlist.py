'''
class Node(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode= b
b.nextnode=c
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
'''
class Doublylinkedlist(object):
  def __init__(self,value):
    self.value = value
    self.nextnode = None
    self.prevnode = None

a = Doublylinkedlist(1)
b = Doublylinkedlist(2)
c = Doublylinkedlist(3)
a.nextnode=b
b.prevnode=a
b.nextnode=c
c.prevnode=b
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(b.prevnode.value)
