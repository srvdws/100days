# given an integral number, n, create a dictionary that creates the square
# of all numbers up to n with n as the key


def maker(di, n):
    for i in range(n + 1):
        di[i] = i ** 2

my_dict = dict()

maker(my_dict, 6)

print(my_dict)



