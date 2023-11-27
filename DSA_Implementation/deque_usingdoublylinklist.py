class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def is_empty(self):
        return self.count==0
    
    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty:
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
        self.count+=1
    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.count+=1
        self.rear=n
    def delete_first(self):
        if self.is_empty():
            raise IndexError("empty")
        if self.count==1:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.count-=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("empty")
        if self.count==1:
            self.front,self,rear=None,None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.rear.item
    def size(self):
        return self.count
d=Dequeue()
d.insert_front(1)
d.insert_rear(2)
print(d.get_front())
print(d.get_rear())
    
    
        




            
            
        

            
            
            
        
