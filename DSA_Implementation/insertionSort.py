def insertion(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and key<l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
l=[2,4,8,6]
insertion(l)
print(l)
            
