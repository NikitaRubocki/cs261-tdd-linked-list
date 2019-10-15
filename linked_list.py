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
        return self.is_sentinel()

    def last(self):
        if self.is_last():
            return self
        return self.next.last()
     
    def append(self, node):
        if self.is_empty():
            self.value = node
            self.next = node
            self.prev = node
            node.value = None
            node.next = self
            node.prev = self
            return
        # if self.is_last():
        #     self.value = node
        #     node.value = None
        #     self.next = node
        #     node.prev = self
        # else:
        #     self.prev = node
        #     node.next = self
        #     # self = self.next
        #     self.next.append(node)
        self.prev = node
        node.next = self
        self = self.last()
        self.value = node
        node.value = None
        self.next = node
        node.prev = self