class Graph:
    def __init__(self,vno):
        self.v_count=vno
        self.adj_matrix=[[0]*vno for  e in range(vno)]
    def add_edge(self,u,v,w=1):
        if 0<=u<self.v_count and  0<=v<self.v_count:
            self.adj_matrix[u][v]=w
            self.adj_matrix[v][u]=w
        else:
            print("invalid Vertex")
            
    def remove_edge(self,u,v):
        if 0<=u<self.v_count and  0<=v<self.v_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid Vertex")
    def has_edge(self,u,v):
        if 0<=u<self.v_count and  0<=v<self.v_count:
            return self.adj_matrix[u][v]!=0
        
        else:
            print("invalid Vertex")
    def print_adj_matrix(self):
        for i in self.adj_matrix:
            print(" ".join(map(str,i)))
            

g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_matrix()
