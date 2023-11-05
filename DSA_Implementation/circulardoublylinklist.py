class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

        

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def print(self):
        if self.start is None:
            print("empty")
        else:
            tmp=self.start
            while(tmp!=self.start.prev):
                print(tmp.item,end=" ")
                tmp=tmp.next
            print(tmp.item)

    def search(self,data):
        if self.start is None:
            return None
        else:
            tmp=self.start
            while(tmp!=self.start.prev):
                if tmp.item==data:
                    return tmp
                tmp=tmp.next
            if tmp.item==data:
                return tmp
            return None


    def insert_start(self,data):
        n=Node()
        n.item=data
        if self.start is None:
            self.start=n
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev=n
            self.start=n


    def insert_end(self,data):
        if self.start is None:
            self.insert_start(data)
        else:
            n=Node()
            n.item=data
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n

    def delete_start(self):
        if self.start is None:
            pass
        elif self.start.next==self.start:
            self.start=None
        else:
            self.start.prev.next=self.start.next    
            self.start.next.prev=self.start.prev
            self.start=self.start.next
    def delete_end(self):
        if self.start is None:
            pass
        elif self.start==self.start.next:
            self.start=None
        else:
            self.start.prev.next=self.start
            self.start.prev=self.start.prev.prev


              
        


cdl=CDLL()
cdl.insert_start(2)
cdl.insert_start(1)
cdl.insert_start(0)
cdl.insert_end(4)
cdl.insert_start(-1)
cdl.insert_end(5)
cdl.print()
cdl.delete_end()
cdl.print()
cdl.delete_end()
cdl.print()
    