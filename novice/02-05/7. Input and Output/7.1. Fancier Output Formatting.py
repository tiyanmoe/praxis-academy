year = 2016
event = 'merupakan kelulusan SMK dari Tiyanmoe'
print(f'Pada tahun {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}' .format(yes_votes, percentage))

s = "Halodek"
print(str(s))
print(repr(s))
print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'Nilai dari X adalah ' +repr(x) + ', dan Y adalah ' +repr(y) + '...'
print(s)
# the argument to repr() may be any Python object
print(repr((x, y, ('nyampah', 'terosss'))))

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, btch\n'
hellos = repr(hello)
print(hellos)
