class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.next=next
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.count=0
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            tmp=self.start
            while tmp.next and temp.next.priority<=priority:
                tmp=tmp.next
            n.next=tmp.next
            tmp.next=n
        self.count+=1
    def is_empty(self):
        return self.count==0
    def pop(self):
        if self.is_empty():
            raise IndexError("empty list")
        data=self.start.item
        self.start=self.start.next
        self.count-=1
        return data
    def size(self):
        return self.count
pq=PriorityQueue()
pq.push(10,2)
pq.push(20,1)
print(pq.pop())

            
        
