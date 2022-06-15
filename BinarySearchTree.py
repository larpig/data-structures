class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            # Added value already exists
            return

        if data < self.data:
            # Added value is less than that from the current node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Added value is greater than that from the current node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, data):
        if data == self.data:
            # Searched value is equal to that from the current node
            return True

        if data < self.data:
            # Searched value is less than that from the current node
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            # Searched value is greater than that from the current node
            if self.right:
                return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        return sum(self.in_order_traversal())


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print("The minimum value is :", numbers_tree.find_min())
    print("The maximum value is :", numbers_tree.find_max())
    print("The sum of all values is:", numbers_tree.calculate_sum())

    numbers_tree = build_tree([15, 27, 12, 7, 14, 88, 20, 23])
    print("Pre order traversal gives this sorted list:", numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:", numbers_tree.post_order_traversal())