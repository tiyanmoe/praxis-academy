t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
    # print(t[0] = 88888) --- sintak error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)


empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

# x, y, z = t