def bubbleSort(l):
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

l=[30,2,6,3,27,9,1,0,2]
print(l)
bubbleSort(l)
print("After sorting")
print(l)
