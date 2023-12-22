# program to print first n natural number

def firstnatural(n):
    if n==0:
        return
    firstnatural(n-1)
    print(n)
#firstnatural(5)




def firstnatural_reverse(n):
    if n==0:
        return
    print(n)
    firstnatural_reverse(n-1)
#firstnatural_reverse(5)


def firstnodd(n):
    if n==0:
        return
    firstnodd(n-1)
    print(2*n-1)
#firstnodd(5)

def firstneven(n):
    if n==0:
        return
    firstneven(n-1)
    print(2*n)
#firstneven(5)


def firstnodd_rev(n):
    if n==0:
        return
    print(2*n-1)
    firstnodd_rev(n-1)
    
#firstnodd_rev(5)

def firstneven_rev(n):
    if n==0:
        return
    print(2*n)
    firstneven_rev(n-1)
  
firstneven_rev(5)


