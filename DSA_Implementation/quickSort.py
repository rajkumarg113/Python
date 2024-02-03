def partition(arr,l,h):
    i=l-1
    pivot=arr[h]
    for j in range(l,len(arr)):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

arr=[3,11,63,4,50,24,28,63]

def qsort(arr,l,h):
    if l<h:
        p=partition(arr,0,h)
        qsort(arr,l,p-1)
        qsort(arr,p+1,h)
print(arr)
qsort(arr,0,len(arr)-1)
print("After sorting")
print(arr)
