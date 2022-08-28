print(sum(i*i for i in range(10)))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product

# unique_words = set(word for line in page  for word in line.split())
# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))