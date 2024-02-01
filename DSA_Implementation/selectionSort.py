def selection(l):
    for i in range(0,len(l)-1):
        min_idx=i
        for j in range(i+1,len(l)):
            if l[j]<l[min_idx]:
                min_idx=j
        l[i],l[min_idx]=l[min_idx],l[i]
l=[2,4,5,6,1,56,99,0,7,21]
selection(l)
print(l)
        
                       
            
