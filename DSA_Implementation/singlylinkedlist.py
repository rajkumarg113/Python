class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty:
            self.start=n
        else:
            curr=self.start
            while curr.next!=None:
                curr=curr.next
            curr.next=n
    def search(self,data):
        if self.is_empty():
            return "Not Find"
        tmp=self.start
        while tmp.next!=None:
            if tmp.item==data:
                return tmp
            tmp=tmp.next
        return None
    def insert_after(self,tmp,data,):
        if tmp is not None:
            n=Node(data,tmp.next)
            tmp.next=n
    def print_list(self):
        tmp=self.start
        while tmp!=None:
            print(tmp.item,end=" ")
            tmp=tmp.next
        print("\n")

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            tmp=self.start
            while(tmp.next.next!=None):
                tmp=tmp.next
            tmp.next=None
    def delete_item(self,data):
        if self.start==None:
            pass
        elif self.start.next==None:
            if self.start.item==data:
                self.start=None
        else:
            tmp=self.start
            if tmp.item==data:
                self.start=tmp.next
            else:
                while tmp.next.item!=data and tmp.next!=None:
                    tmp=tmp.next
                tmp.next=tmp.next.next

    def __iter__(self):
        return SLLIterable(self.start)

#now making our singly linked list iterable

class SLLIterable:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data=self.current.item
            self.current=self.current.next
            return data
    
if __name__=="__main__":
    Slist=SLL()
    Slist.insert_at_start(7)
    Slist.insert_at_start(4)
    Slist.insert_at_start(3)
    Slist.print_list()
    Slist.insert_after(Slist.search(4),5)
    Slist.print_list()
    Slist.delete_first()
    Slist.print_list()
    Slist.insert_at_start(3)
    Slist.print_list()
    Slist.delete_last()
    Slist.print_list()
    Slist.delete_item(4)
    Slist.print_list()
    Slist.insert_after(Slist.search(3),4)
    Slist.print_list()
    Slist.delete_item(3)
    Slist.print_list()
    for i in Slist:
        print(i)
    


            


