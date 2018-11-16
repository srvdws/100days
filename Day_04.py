# enter a series of comma seperated numbers, convert to list, convert to tuple
teststring = "7,5,3,1,5,9,8,2,4"


my_list = teststring.split(",")
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)