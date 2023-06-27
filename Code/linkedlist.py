#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, item):
        node = self.head
        while node:
            if node.data == item:
                return node.data
            node = node.next
        return None

    def delete(self, item):
        if self.is_empty():
            raise ValueError(f'Item not found: {item}')

        if self.head.data == item:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            return

        node = self.head
        while node.next and node.next.data != item:
            node = node.next

        if node.next is None:
            raise ValueError(f'Item not found: {item}')
        else:
            node.next = node.next.next
            if node.next is None:
                self.tail = node
    def replace(self, old_item, new_item):
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next
        print(f'Item not found: {old_item}')

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
