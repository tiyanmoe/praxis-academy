# Fibonacci numbers module

# ini adalah struktur fungsi pertama
def fib(n) :    # write Fibonacci series ip to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# ini adalah struktur fungsi kedua
def fib2(n):    # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result