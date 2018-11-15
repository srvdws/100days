# given an integral number, n, create a dictionary that creates the square
# of all numbers up to n with n as the key


def make_dict(di, n):
    for i in range(n+1):
        di[i] = i ** 2


my_di = dict()
make_dict(my_di, 7)

print(my_di)



# def make_dict(di, n):
#     for i in range(n):
#         di[i] = i ** 2
#
#
# my_dict = dict()
#
# make_dict(my_dict, 6)
#
# print(my_dict)
