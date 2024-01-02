def BinaryTree(r):
  return [r,[],[]]

def insertleft(root,newBranch):
  t = root.pop(1)
  if len(t)>1:
    root.insert(1,[newBranch,t,[]])

  else:
    root.insert(1,[newBranch,[],[]])

  return root

def insertright(root,newBranch):
  t = root.pop(1)
  if len(t)>1:
    root.insert(1,[newBranch,[],t])

  else:
    root.insert(1,[newBranch,[],[]])

  return root

def getRootVal(root):
  return root[0]

def setRootVal(root,newVal):
  root[0] = newVal

def getleftchild(root):
  return root[1]

def getrightchild(root):
  return root[2]