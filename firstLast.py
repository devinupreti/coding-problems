def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# PROBLEM : cons(a, b) constructs a pair,
#           and car(pair) and cdr(pair) returns the first and last element of that pair.
#           For example, car(cons(3, 4)) returns 3,
#                        and cdr(cons(3, 4)) returns 4

# Implement car and cdr.

def identity(a,b):
    return (a,b)

def car(pair):
    a,_ = pair(identity)
    return a

def cdr(pair):
    _,b = pair(identity)
    return b

print(car(cons(3,4) ))
print(cdr(cons(3,4) ))
