class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

  def get_next_node(self):
    return self.next_node

  def get_value(self):
    return self.value

class Queue:

  def __init__(self, head_node = None, tail_node = None, limit = 5):
    self.size = 0
    self.limit = limit
    self.head_node = head_node
    self.tail_node = tail_node

  def enqueue(self, new_node):
    if self.limit <= self.size:
      print("Queue Overflow: No room for another!")
      return
    elif self.tail_node == None:
      self.head_node = new_node
      self.tail_node = new_node
    else:
      self.tail_node.set_next_node(new_node)
      self.tail_node = new_node
    tail_value = self.tail_node.get_value()
    print ("Adding complete. The new tail node is %s." % tail_value)
    self.size += 1
    return

  def dequeue(self):
    if self.head_node == None:
      print("Queue Underflow: The queue is already empty.")
    else:
      box = self.head_node.get_value()
      print("Letting out %s." % box)
      self.head_node = self.head_node.get_next_node()
      self.size -= 1
      return box

  def peek(self):
    if self.head_node == None:
      print("There's nothing to peek at!")
    else:
      head_value = self.head_node.get_value()
      print("Successfully peeked.")
      print("Proudly marching at the start of the queue: %s." % head_value)
      return head_value


vily = Node("Vily")
totomato = Node("Totomato")
frankie = Node("Frankie")
francesca = Node("Francesca")
frances = Node("Frances")
yuyu = Node("Yuyu")



queue = Queue()
queue.peek()
queue.enqueue(yuyu)
queue.enqueue(frances)
queue.enqueue(francesca)
queue.enqueue(frankie)
queue.enqueue(totomato)
queue.enqueue(vily)
queue.peek()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.peek()
queue.dequeue()
queue.peek()
queue.dequeue()
queue.dequeue()
