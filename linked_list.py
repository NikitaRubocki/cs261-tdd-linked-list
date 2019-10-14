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
        if self.value is None:
            return True
        return False
