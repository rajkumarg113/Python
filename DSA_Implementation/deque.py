class Dequeue:
    def __init__(self):
        self.d=[]
    def is_empty(self):
        return len(self.d)==0
    def insert_front(self,data):
        self.d.insert(0,data)
    def insert_rear(self,data):
        self.d.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.d.remove(l[0])
    def delete_rear(self):
        if not self.is_empty():
            self.d.pop()
    def get_front(self):
        if not self.is_empty():
            return self.d[0]
    def get_rear(self):
        if not self.is_empty():
            return self.d[len(self.d)-1]
d=Dequeue()
d.insert_front(2)
d.insert_rear(3)
print(d.get_rear())
