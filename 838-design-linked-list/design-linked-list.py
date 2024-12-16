class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >=self.length or index < 0:
            return -1
        head = self.head
        for i in range(index):
            head = head.next
        return head.value
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def addAtIndex(self, index: int, value: int) -> None:
        if index > self.length:
            return 
        elif index == 0:
            self.addAtHead(value)
            return 
        elif index == self.length:
            self.addAtTail(value)
            return 
        else:
            new_node = Node(value)
            temp = self.head
            prev = temp
            for i in range(index):
                prev = temp
                temp = temp.next
            new_node.next = temp
            prev.next = new_node
        self.length +=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            if temp.next is None:
                self.tail = temp
        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)