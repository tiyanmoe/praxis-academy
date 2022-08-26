while True:
    try:
        x = int(input("Please enter a number guis: "))
        break
    except ValueError:
        print("Eh! That was no valid number. Please Try again...")

    except (RuntimeError, TypeError, NameError):
        pass



class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")



import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


# ini kodingan error
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readline()), 'lines')
#         f.closed()



try:
    raise Exception('spam', 'cui')
except Exception as inst:
    print(type(inst))       # the exception instance
    print(inst.args)        # arguments stored in .args
    print(inst)             # __str__ allows args to be printed directly,
                            # but may be overridden in exception subclasses
    x, y = inst.args        # unpack args
    print('x =', x)
    print('y =', y)



def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error gais:', err)
