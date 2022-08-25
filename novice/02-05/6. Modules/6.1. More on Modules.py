# pada halaman ini lanjutan untuk import fibo.py
# pada halaman ini akan menghasilkan output yang sama dengan sintak yang berbeda

from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)

import fibo as fib
fib.fib(500)

from fibo import fib as Fibonacci
Fibonacci(500)