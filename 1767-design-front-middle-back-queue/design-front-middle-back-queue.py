class Node:
     def __init__(self, val=0, prev=None, next=None):
         self.val = val
         self.prev = prev
         self.next = next

class FrontMiddleBackQueue:
    def __init__(self):
        self.head = None
        self.middle = None
        self.tail = None
        self.cnt = 0            

    def pushBack(self, val: int) -> None:
        if not self.cnt:
            self.add_first(val)
            return
            
        new_node = Node(val, self.tail, None)
        self.tail.next = new_node            
        self.tail = new_node
        if self.cnt % 2 == 0:            
            self.middle = self.middle.next
        self.cnt += 1        

    def pushMiddle(self, val: int) -> None:
        if not self.cnt:
            self.add_first(val)
            return
        
        if self.cnt % 2 == 1:
            new_node = Node(val, self.middle.prev, self.middle)
            if self.middle.prev:
                self.middle.prev.next = new_node
            self.middle.prev = new_node
            if self.cnt == 1:
                self.head = new_node
            self.cnt += 1
            self.middle = new_node
        else:
            new_node = Node(val, self.middle, self.middle.next)
            if self.middle.next:
                self.middle.next.prev = new_node
            self.middle.next = new_node
            self.cnt += 1
            self.middle = new_node

    def pushFront(self, val: int) -> None:
        if not self.cnt:
            self.add_first(val)
            return
        
        new_node = Node(val, None, self.head)        
        self.head.prev = new_node        
        self.head = new_node
        
        if self.cnt % 2 == 1:            
            self.middle = self.middle.prev
            
        self.cnt += 1                 

    def popBack(self) -> int:
        if not self.cnt:
            return -1
        elif self.cnt == 1: 
            return self.remove_last()
        
        node = self.tail        
        self.tail = self.tail.prev        
        self.tail.next = None
        
        if self.cnt % 2 == 1:
            self.middle = self.middle.prev        
            
        self.cnt-=1                
        
        return node.val

    def popMiddle(self) -> int:
        if not self.cnt:
            return -1
        elif self.cnt == 1: 
            return self.remove_last()
        
        node = self.middle
        if self.middle.prev:
            self.middle.prev.next = self.middle.next        
        
        self.middle.next.prev = self.middle.prev
        if self.head == self.middle:
            self.head = self.head.next        
            
        if self.cnt % 2 == 0:
            self.middle = self.middle.next
        else:
            self.middle = self.middle.prev
            
        self.cnt-=1        
            
        return node.val        

    def popFront(self) -> int:
        if not self.cnt:
            return -1
        elif self.cnt == 1: 
            return self.remove_last()
        
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        
        if self.cnt % 2 == 0:
            self.middle = self.middle.next        
            
        self.cnt-=1        
        
        return node.val
    
    def add_first(self, val) -> None:
        new_node = Node(val, None, None)
        self.cnt = 1
        self.head =  new_node
        self.middle = new_node
        self.tail = new_node
        
    def remove_last(self) -> None:
        node = self.head
        self.cnt = 0
        self.head = None
        self.middle = None
        self.tail = None
        return node.val



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()