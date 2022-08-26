# sintak 1 
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')



# sintak 2 
def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return())



# sintak 3
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide("2", "1")