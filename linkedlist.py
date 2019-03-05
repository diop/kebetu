#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0 # Length
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty. - 0(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst running time: O(n) for n nodes in the list
        because we have to iterate over all n nodes and count 1 for each"""
        # Loop through all nodes and count one for each
        count = 0
        # node = self.head
        # while node  is not None:
        #     count += 1
        #     node = node.next
        for bucket in self.buckets: #0(n)
            count += bucket.length() # 0(l)
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst running timme: O(1) - only change the tail node"""
        # Create new node to hold given item
        # Append node after tail, if it exists
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        # Update tail to new node regardless
        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worth case running time: O(1) because we only change
        the first node and never loop through all nodes"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        node = Node(item)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or not 
        present, and we need to loop through all n nodes in the list"""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            print(quality)
            if quality(node.data):
                print(node.data)
                return node.data
            node = node.next
        return None
        
    # Delete Code attribution: https://github.com/anselb/Tweet-Generator/blob/master/source/linkedlist.py
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current_node = self.head
        deleted = False
        previous = None
        while current_node is not None:
            if current_node.data == item and current_node is self.head and current_node is self.tail:
                self.head = None
                self.tail = None 
                deleted = True 
            elif current_node.data == item and current_node is self.head:
                self.head = current_node.next
                if self.head == self.tail:
                    self.tail = current_node.next
                deleted = True
            elif current_node.data == item and current_node is self.tail:
                self.tail = previous 
                self.tail.next = None 
                if self.head == self.tail:
                    self.head = previous
                deleted = True
            elif current_node.data == item:
                previous.next = current_node.next
                deleted = True

            previous = current_node
            current_node = current_node.next
        
        if not deleted:
            raise ValueError('Item not found: {}'.format(item))



        

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()