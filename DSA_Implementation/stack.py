class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            self.item.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.item)
    
s=Stack()
s.push(2)
s.push(3)
print(s.peek())
s.pop()
print(s.peek())