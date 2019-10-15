# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Nikita Rubocki

class LinkedList:

    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self
    
    def is_sentinel(self):
        if self.value is not None:
            return False
        return True

    def is_empty(self):
        if self.next is not self or self.prev is not self:
            return False
        return True
    
    def is_last(self):
        if self.next.is_sentinel():
            return True
        return False

    def last(self):
        if self.is_last():
            return self
        return self.next.last()
    
    def _linkEmptyList(self, node):
        self.next = node
        self.prev = node
        node.next = self
        node.prev = self
    
    def append(self, node):
        if self.is_empty():
            self._linkEmptyList(node)
            return
        # link "front" node and new node together
        self.prev = node
        node.next = self
        # set "front" node to "last" node
        self = self.last()
        # link "last" node and new node
        self.next = node
        node.prev = self

    def delete(self):
        # hold the pointers for the node being deleted
        prev_node = self.prev
        next_node = self.next
        # set self to prev node
        self = self.prev
        # set prev node to point "over" the deleted node to next
        self.next = next_node
        # set self to next node
        self = self.next
        # set next node to point "over" the deleted node to prev
        self.prev = prev_node

    def insert(self, node):
        next_node = self.next
        # prev node links to new node
        self.next = node
        # new node links to prev node
        node.prev = self
        # set self to next node
        self = next_node
        # next node links to new node 
        self.prev = node
        # new node links to next node 
        node.next = self

    def insert_in_order(self, node):
        if self.is_empty():
            return self.append(node)
        if self.is_sentinel() is False and self.value > node.value:
            return self.prev.insert(node)
        if self.is_sentinel() is False and self.value < node.value:
            return self.insert(node)
        return self.next.insert_in_order(node)



    def at(self, num, n=0):
        if n == num:
            return self
        n += 1
        return self.next.at(num, n)

    def search(self, value):
        if self.value == value:
            return self
        if self.is_last():
            return None
        return self.next.search(value)    