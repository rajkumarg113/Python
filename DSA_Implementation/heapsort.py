class Heap:
    def __init__(self):
        self.heap=[]
    def create_heap(self,list1):
        for e in list1:
            self.insert(e)
    def insert(self,e):
        index=len(self.heap)
        parentIndex=index-1//2
        while index>0 and self.heap[parentIndex]<=e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def 
