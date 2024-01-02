class HashTable(object):
  def __init__(self,size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots))
    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data

    else:
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data

      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot,len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot] = key
          self.data[nextslot] = data
          
          
    
    