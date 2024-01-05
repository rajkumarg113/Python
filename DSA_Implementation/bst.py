class Node:
    def __init__(self,item=None,left=None,right=None):
        self.left=left
        self.item=item
        self.right=right
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<=root.item:
            root.left=self.rinsert(root.left,data)
        elif data>=root.item:
            root.right=self.rinsert(root.right,data)
        return root
    
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        if data>root.item:
            return self.rsearch(root.right,data)
    def inorder(self):
        self.rinorder(self.root)
    def rinorder(self,root):
        if root is None:
            return
        self.rinorder(root.left)
        print(root.item)
        self.rinorder(root.right)
        
    def preorder(self):
        self.rpreorder(self.root)
    def rpreorder(self,root):
        if root is None:
            return
        print(root.item)
        self.rpreorder(root.left)
        self.rpreorder(root.right)
        
    def postorder(self):
        self.postorder(self.root)
    def rpostorder(self,root):
        if root is None:
            return
        self.rpostorder(root.left)
        self.rpostorder(root.right)
        print(root.item)
    def min_value(self,root):
        tmp=root
        while(tmp.left is not None):
            tmp=tmp.left
        return tmp.item
    def max_value(self,root):
        tmp=root
        while(tmp.right is not None):
            tmp=tmp.right
        return tmp.item
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
        
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left= self.rdelete(root.left,data)
        elif data>root.item:
            root.right= self.rdelet(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.item=self.min_value(root.right)
                root.right=self.rdelete(root.right.root.item)
                self.rdelete(root.right,root,item)
            return root
    def count_node(self,root):
        if root is None:
            return 0
        return 1+self.count_node(root.left)+self.count_node(root.right)
        
            
            
        
     

bt=BST()
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(50)
bt.insert(60)
bt.inorder()
print(bt.count_node(bt.root))
