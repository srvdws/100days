# enter a series of comma seperated numbers, convert to list, convert to tuple
teststring = "7,5,3,1,5,9,8,2,4"


my_str = teststring

my_list = my_str.split(",")
my_tuple = tuple(sorted(int(i) for i in my_list))


print(my_list)
print(my_tuple)

# my_input = teststring
#
# my_list = my_input.split(",")
# my_tuple = tuple(my_list)
#
# print(my_list)
# print(my_tuple)