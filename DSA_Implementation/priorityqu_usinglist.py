class PriorityQueue:
    def __init__(self):
        self.p=[]
    def is_empty(self):
        return len(self.p)==0
    def push(self,data,priority):
        index=0
        while index<len(self.p) and self.p[index][1]<=priority:
            index+=1
        self.p.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty")
        return self.p.pop(0)[0]
    def size(self):
        return len(self.p)

pq=PriorityQueue()
pq.push(10,1)
pq.push(20,0)

while not pq.is_empty():
    print(pq.pop())
        
