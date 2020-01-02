# Implement queue using linked list is better.
# if we use python list then the running cost will be more.
# Cause If the first element is moved then all the element in the queue has to move on step ahed
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../1.4 Linked List/')

from Linked_list import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, element):
        return self.queue.insert_at_tail(element)

    def dequeue(self):
        return self.queue.delete_at_head().get_value()

    def is_empty(self):
        return self.queue.is_empty()

    def have_element(self, element):
        return self.queue.have_element(element)

    def __sizeof__(self):
        return self.queue.__sizeof__()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.have_element(1))