# find all numbers divisible by 7 but NOT divisible by 5 between 2000 and 3200
# solution: csv single line


my_list = list()


for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        my_list.append(i)


print(my_list)
