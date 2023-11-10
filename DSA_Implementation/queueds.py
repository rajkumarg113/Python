class queue:
    def __init__(self):
        self.myq=[]
        self.front=-1
        self.rear=-1
    def is_empty(self):
        return len(self.myq)==0
    def enqueue(self,data):
        self.myq.append(data)
    def dequeue(self):
        if(self.is_empty()==False):
            self.myq.remove(self.myq[0])
        else:
            raise IndexError("queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.myq[0]
        else:
            raise IndexError
    def get_rear(self):
        if not self.is_empty():
            return self.myq[-1]
        else:
            raise IndexError("queue is empty")
    def size(self):
        return len(self.myq)
    
        
q1=queue()
q1.enqueue(1)
q1.enqueue(2)
print(q1.get_front())
q1.enqueue(3)
print(q1.get_rear())



    
