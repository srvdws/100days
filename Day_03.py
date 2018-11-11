# given an integral number, n, create a dictionary that creates the square of all numbers up to n with n as the key


n = int(input('enter a number: '))
my_dictionary = dict()

for i in range(1, n+1):
    my_dictionary[i] = (i ** 2)

print(my_dictionary)
