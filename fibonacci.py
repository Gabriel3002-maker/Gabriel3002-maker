#forma iteractiva
def fib(n):
    a = 0
    b = 1
    for k in range(n):
        c = a +b
        a = b 
        b = c 
    return b

for x in range(20):
    print(fib(x))

#forma recursiva
def fib_r(n):
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)

for x in range(20):
    print(fib_r(x))