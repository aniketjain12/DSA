import collections
class Node:
  def __init__(self,val=None):
    self.left = None
    self.right = None
    self.val = val

def levelOrderPrint(tree):
    if not tree:
      return

    node = collections.deque([tree])
    currentCount = 1
    nextCount = 0
    while len(node) != 0:
      currentNode = node.popleft()
      currentCount -=1
      print(currentNode.val)
      if currentNode.left:
        node.append(currentNode.left)
        nextCount += 1

      if currentNode.right:
        node.append(currentNode.right)
        nextCount += 1

      if currentNode == 0:
        print('\n')

      currentCount,nextCount = nextCount,currentCount

root = Node(1)
root.left = Node(2)
root.right = Node(3)
levelOrderPrint(root)