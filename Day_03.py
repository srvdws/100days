# given an integral number, n, create a dictionary that creates the square
# of all numbers up to n with n as the key


def maker(di, n):
    for i in range(n):
        di[i] = i ** 2

my_d = dict()
maker(my_d, 12)

print(my_d)



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
