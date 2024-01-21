def bubbleSort(l):
    for i in range(len(l)):
        flag=False
        for j in range(0,len(l)-i-1):
            if(l[j]>l[j+1]):
                flag=True
                l[j],l[j+1]=l[j+1],l[j]
        if not flag:
            break
            

l=[30,2,6,3,27,9,1,0,2]
print(l)
bubbleSort(l)
print("After sorting")
print(l)
