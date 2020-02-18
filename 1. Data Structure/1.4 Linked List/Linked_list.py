class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size:
            return -1
        current_index = 0
        current_node = self.head
        while current_index <= index:
            if current_index == index:
                return current_node.val
            elif current_node.next is None:
                return -1
            else:
                current_node = current_node.next
                current_index += 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.size == 0:
            return self.addAtHead(val)
        current_node = self.head
        while current_node is not None:
            if current_node.next == None:
                # This is tail
                new_node = Node(val, None)
                current_node.next = new_node
                self.size += 1
                return
            current_node = current_node.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)
        elif index > self.size:
            return
        current_node = self.head
        previous_node = None
        for current_index in range(index + 1):
            if current_index == index:
                # Insert before this
                previous_node.next = Node(val, current_node)
                self.size += 1
                return
            previous_node = current_node
            current_node = current_node.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        if index >= self.size:
            return
        current_node = self.head
        previous_node = None
        for current_index in range(index + 1):
            if current_index == index:
                previous_node.next = current_node.next
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
obj.addAtHead(7)
obj.deleteAtIndex(1)
obj.addAtHead(3)
obj.addAtHead(3)
obj.addAtHead(3)
obj.addAtHead(3)
obj.addAtHead(3)
obj.addAtHead(3)
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)