import math
print(f'The values of pi is approximately {math.pi:.3f}.')


table = {'Syahrin': 4127, 'Baskoro': 4098, 'Tiyanmoe': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


animals = 'topi miring'
print(f'Cintaku pahamu sepahit {animals}.')
print(f'Cintaku padamu sepahit {animals!r}.')