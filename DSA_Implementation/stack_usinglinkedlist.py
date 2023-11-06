class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=None

class Stack:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0

    def is_empty(self):
        return self.start==None
    def push(self,data):
        n=Node(data)
        if self.start==None:
            self.start=n
            n.next=None
            self.item_count+=1
        else:
            n.next=self.start
            self.start=n
            self.item_count+=1
    def pop(self):
        if self.start is None:
            raise IndexError("Stack is empty")
        else:
            self.start=self.start.next
            self.item_count-=1
    def peek(self):
        if self.start is None:
            raise IndexError("stack is empty")
        else:
            return self.start.item
    def size(self):
        return self.item_count
    
s=Stack()
s.push(1)
s.push(2)
print(s.peek())
s.pop()
print(s.peek())

