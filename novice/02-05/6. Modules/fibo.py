# Fibonacci numbers module

# koding define yang sudah ada perintah print
def fib(n) :    # write Fibonacci series ip to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# koding ini define return/result harus ditambah print pada saat running program
def fib2(n):    # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))