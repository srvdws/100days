# given an integral number, n, create a dictionary that creates the square
# of all numbers up to n with n as the key

my_dict = dict()


def generate_dict(n):
    for i in range(0, n):
        my_dict[i] = i ** 2


generate_dict(5)
print(my_dict)
