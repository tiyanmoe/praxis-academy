f = open('workfile', 'w', encoding="utf-8")
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# dibawah ini adalah salah satu koding error
# print(f.close())
# print(f.read())