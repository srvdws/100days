# take 2 digits, x and y as inputs and generate a two dimensional array of the value of x and y multiplied


my_input = (input("two ints(x,y): ").split(","))
print(my_input)


rows = int(my_input[0])
cols = int(my_input[1])



new_list = [["X" for r in range(rows)] for c in range(cols)]


for col in range(cols):
    for row in range(rows):
        new_list[col][row] = row * col

for i in new_list:
    print(i)


# my_input = (input("x, y").split(","))
#
# xval = int(my_input[0])
# yval = int(my_input[1])
#
# e_list = [["0" for col in range(xval)] for row in range(yval)]
#
# for row in range(yval):
#     for col in range(xval):
#         e_list[row][col] = row * col
#
# for i in e_list:
#     print(i)










# sys_input = input("::")
#
# dimension = [int(x) for x in sys_input.split(",")]
#
# rowin = dimension[0]
# colin = dimension[1]
#
# my_list = [[0 for i in range(rowin)] for d in range(colin)]
# new_list = my_list
#
# for col in range(colin):
#     for row in range(rowin):
#         my_list[col][row] = row * col
#
# for i in new_list:
#     print(i)

