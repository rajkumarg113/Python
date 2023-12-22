def sumn(n):
    if n<=0:
        return 0
    return n+sumn(n-1)
#print(sumn(5))

def sumn_odd(n):
    if n<=0:
        return 0
    return (2*n-1)+sumn_odd(n-1)
#print(sumn_odd(5))



def sumn_even(n):
    if n<=0:
        return 0
    return (2*n)+sumn_even(n-1)
#print(sumn_even(5))


def factorial(n):
    if n<=0:
        return 1
    return n*factorial(n-1)
#print(factorial(5))


def sumn_sq(n):
    if n<=0:
        return 0
    return n*n+sumn_sq(n-1)
print(sumn_sq(3))

    
