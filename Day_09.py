# create an array of 5 integers and display array itms, acces tehm via index

from array import *
array_num = array('i', [1,3,5,7,9])

for i in array_num:
    print(i)

print(array_num[0])
print(array_num[1])
print(array_num[2])

# append a new item to the end of the array:

array_num.append(11)
print(array_num)

# print reverse the order:

print(array_num[::-1])

#insert a new value before the number 3:

array_num.insert(array_num.index(3), 4)
print(array_num)

# remove an itme via index

array_num.pop(2)
print(array_num)

#remove the first ocucurance of an element

print("\nnew_ arry: \n")
new_array = array("i", [1,3,5,7,3,9,3,11])
print(new_array)
new_array.remove(3)
print(new_array)


# convert an array into a list
print("\ntype\n")

print(type(new_array))
x = new_array.tolist()
print(type(x))






