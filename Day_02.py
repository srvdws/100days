# Derive function


def this(n):
    if n == 0:
        return 1
    else:
        return n * this(n-1)


print(this(18))
