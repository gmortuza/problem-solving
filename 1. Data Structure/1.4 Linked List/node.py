class Node:
    def __init__(self, value):
        self.next_node = None
        self.value = value

    def set_value(self, element):
        self.value = element

    def get_value(self):
        return self.value

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self) :
        return self.next_node