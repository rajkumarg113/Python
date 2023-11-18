class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=None
class Queue:
    def __init__(self):
        self.count=0
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(data)
        if self.count==0:
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        elif(self.front==self.rear):
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.rear.item

    def size(self):
        return self.count
q=Queue()

q.enqueue(10)
q.enqueue(20)
print(q.get_front())
print(q.get_rear())









        
    
            
        
    
