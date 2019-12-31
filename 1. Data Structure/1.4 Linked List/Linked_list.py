from node import Node

class LinkedList:

    def __init__(self):
        self.head = self.tail = None

    def insert_at_head(self, element) -> None:
        if self.is_empty():
            self.__set_first_element(element)
        else:
            node = Node(element)
            node.set_next(self.head)
            self.head = node

    def insert_at_tail(self, element) -> None:
        if self.is_empty():
            self.__set_first_element(element)
        else:
            node = Node(element)
            self.tail.set_next(node)
            self.tail = node

    def delete_at_head(self):
        if self.is_empty():
            return None
        head = self.head
        self.head = head.get_next()
        return head

    def delete_at_tail(self):
        if self.is_empty():
            return None
        current_element = self.head  # Start the looping from the head
        # For singly linked list this operation would be O(n)
        while True:  # we will keep looking untill we get the next element as tail
            if current_element.get_next() == self.tail:
                self.tail = current_element
                return self.tail
            current_element = current_element.get_next()
        pass

    def have_element(self, element):
        # This will return only the first index
        current_element = self.head
        while True:
            if current_element.get_value() == element:
                return True
            elif current_element == self.tail:
                return False
            current_element = current_element.get_next()

    def is_empty(self):
        return self.head == self.tail is None

    def __set_first_element(self, element):
        node = Node(element)
        self.head = self.tail = node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(3)
    ll.insert_at_head(5)
    ll.insert_at_head(5)
    ll.insert_at_head(5)
    ll.insert_at_tail(5)
    ll.delete_at_head()
    ll.delete_at_tail()
    hav = ll.have_element(10)
    print(ll)