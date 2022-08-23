def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def foo(name, **kwds):
    return 'name' in kwds

def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True