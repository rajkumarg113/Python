class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def print(self):
        tmp=self.start
        while tmp is not None:
            print(tmp.item,end=" ")
            tmp=tmp.next
        print("\n")

    def search(self,data):
        if self.start==None:
            return None
        else:
            tmp=self.start
            while(tmp!=None):
                if tmp.item==data:
                    return tmp
                tmp=tmp.next
        return None

    def insert_begin(self,data):
        n=Node()
        n.prev=None
        n.item=data
        if self.start == None:
            n.next=None
        else:
            n.next=self.start
            self.start.prev=n
        self.start=n
    def insert_end(self,data):
        n=Node()
        n.item=data
        n.next=None
        if self.start is None:
            n.prev=None
            self.start=n
        else:
            tmp=self.start
            while tmp.next is not None:
                tmp=tmp.next
            tmp.next=n
            n.prev=tmp

    def insert_after(self,tmp,data):
        if tmp is not None:
            n=Node()
            n.item=data
            n.next=tmp.next
            n.prev=tmp
            tmp.next=n
            if n.next!=None:
                n.next.prev=n
        else:
            pass

    def delete_first(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            self.start.next.prev=None
            self.start=self.start.next

    def delete_last(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            tmp=self.start
            while(tmp.next!=None):
                tmp=tmp.next
            tmp.prev.next=None

    def delete_item(self,data):
        if self.start==None:
            pass
        elif self.start.next==None:
            if self.start.item==data:
                self.delete_last()
        else:
            tmp=self.start
            if(tmp.item==data):
                self.delete_first()
            else:
                while(tmp.next.item!=data and tmp.next!=None):
                    tmp=tmp.next
                tmp.next=tmp.next.next
                if(tmp.next is not None):
                    tmp.next.prev=tmp

    def __iter__(self):
        return DLLiterable(self.start)


class DLLiterable:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        else:
            data=self.current.item
            self.current=self.current.next
            return data
        

dl=DLL()
dl.insert_begin(8)
dl.insert_begin(2)
dl.insert_end(15)
dl.print()
dl.delete_item(2)
dl.print()

for i in dl:
    print(i)
