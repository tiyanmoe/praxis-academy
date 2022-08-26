# sintak error
# raise NameError('Hi cuy')
# raise ValueError    # shorthand for 'raise ValueError()
try:
    raise NameError('Hi Cuy')
except NameError:
    print('An Exception flew by!!!')
    raise
