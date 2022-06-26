class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Node({self.data}, {self.next})'


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        # Take the last node
        n = self.get_length()
        node = self.get_node(n - 1)

        new_node = Node(data)
        node.next = new_node

    def insert_at(self, data, index):
        n = self.get_length()

        if index < 0 or index > n - 1:
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)
        else:
            # Take the node before the node to be moved
            node = self.get_node(index - 1)
            new_node = Node(data, node.next)
            node.next = new_node

    def insert_after_value(self, data_to_insert, data_after):
        index = self.get_index_by_value(data_after)
        self.insert_at(data_to_insert, index+1)

    def remove_at(self, index):
        n = self.get_length()

        if index < 0 or index > n - 1:
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
        elif index == n - 1:
            # Take the node before the node to be removed
            node = self.get_node(index - 1)
            node.next = None
        else:
            # Take the node before the node to be removed
            node = self.get_node(index - 1)
            node.next = node.next.next

    def remove_by_value(self, data):
        index = self.get_index_by_value(data)
        self.remove_at(index)

    def get_index_by_value(self, data):
        n = self.get_length()

        index = 0
        node = self.head
        while index < n:
            if node.data == data:
                return index
            node = node.next
            index += 1

        raise Exception('Invalid value')

    def get_node(self, index):
        if index < 0 or index > self.get_length() - 1:
            raise Exception('Invalid index')

        node = self.head
        for i in range(index):
            node = node.next
        return node

    def get_length(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def __str__(self):
        str_ll = ''
        node = self.head
        while node:
            str_ll += str(node.data) + " |--> "
            node = node.next
        return str_ll


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(30)
    print(f'linked list of length: {ll.get_length()}')
    print(f'Get the 0º node: {ll.get_node(0)}')
    ll.insert_at_beginning(50)
    print(f'Insert 50 at beginning: {ll}')
    ll.insert_at_end(40)
    ll.insert_at_end(10)
    print(f'Insert 40 and 10 at end: {ll}')
    ll.remove_at(1)
    print(f'Remove index 1: {ll}')
    ll.insert_at(20, 2)
    print(f'Insert 20 at index 2: {ll}')
    ll.remove_by_value(20)
    print(f'Remove the value 20: {ll}')
    ll.insert_after_value(30, 40)
    print(f'Insert 30 after 40: {ll}')
