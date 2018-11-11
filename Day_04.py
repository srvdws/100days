# enter a series of comma seperated numbers, convert to list, convert to tuple

my_input = input('Enter comma seperated numbers: \n')
my_list = my_input.split(',')
my_tuple = tuple()

for i in range(0, len(my_list)-1):
    my_tuple = tuple(sorted(my_list[:i]))

print(my_list, my_tuple)
