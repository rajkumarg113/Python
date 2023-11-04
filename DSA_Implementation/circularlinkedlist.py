class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None
    
    def print(self):
        if self.last is None:
            print("empty")
        else:
            tmp=self.last.next
            while tmp!=self.last:
                print(tmp.item,end=" ")
                tmp=tmp.next
            print(self.last.item)
    def search(self,data):
        if self.last is None:
            return None
        else:
            tmp=self.last.next
            if(tmp.item==data):
                return tmp
            while(tmp!=self.last):
                if(tmp.item==data):
                    return tmp
                tmp=tmp.next
        return None


    def insert_begin(self,data):
        n=Node()
        n.item=data
        if(self.last==None):
            self.last=n
            n.next=n
            
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_last(self,data):
        n=Node()
        n.item=data
        if self.last is None:
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def insert_after(self,tmp,data):
        if tmp is not None:
            if(tmp==self.last):
                self.insert_last(data)
            else:
                n=Node()
                n.item=data
                n.next=tmp.next
                tmp.next=n

    def delete_first(self):
        if self.last is None:
            pass
        elif self.last.next==self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
    def delete_last(self):
        if self.last is None:
            pass
        elif self.last.next==self.last:
            self.last=None
        else:
            tmp=self.last.next
            while(tmp.next!=self.last):
                tmp=tmp.next
            tmp.next=self.last.next
            self.last=tmp

    def delete_item(self,data):
        if self.last is None:
            pass
        elif self.last.next==self.last:
            if self.last.item==data:
                self.last=None
        else:
            tmp=self.last.next
            while tmp.next.item!=data and tmp.next!=None:
                tmp=tmp.next
            if tmp.next==self.last:
                self.delete_last()
            else:
                tmp.next=tmp.next.next



        
cl=CLL()
cl.insert_begin(2)
cl.insert_begin(1)
cl.insert_begin(0)
cl.insert_last(3)
cl.insert_after(cl.search(3),4)
cl.print()
cl.delete_item(3)
cl.print()

