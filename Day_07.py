# take 2 digits, x and y as inputs and generate a two dimensional array of the value of x and y multiplied

sys_input = input("::")

dimension = [int(x) for x in sys_input.split(",")]

rowin = dimension[0]
colin = dimension[1]

my_list = [["0" for i in range(rowin)] for d in range(colin)]
new_list = my_list

for col in range(colin):
    for row in range(rowin):
        my_list[col][row] = row * col

for i in new_list:
    print(i)

