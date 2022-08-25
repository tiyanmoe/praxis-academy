f.read()
f.read()

f.readline()
f.readline()
f.readline()

for line in f:
    print(line, end='')

f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)

