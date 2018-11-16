# find all numbers divisible by 7 but NOT divisible by 5 between 2000 and 3200
# solution: csv single line


def finder(li):
    for i in range(2000, 2301):
        li.append(i)

my_list = list()

finder(my_list)

print(",".join(str(i) for i in my_list))
