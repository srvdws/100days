# find all number divisible by 7 but NOT 5 between 2000 and 3200
# solution: csv single line

empty_list = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        empty_list.append(str(i))

print(" , ".join(empty_list))
