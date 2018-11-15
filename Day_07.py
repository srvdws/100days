# take 2 digits, x and y as inputs and generate a two- dimensional array

sys_input = input("::")

dimension = [int(x) for x in sys_input.split(",")]

rowin = dimension[0]
colin = dimension[1]

my_list = [["0" for i in range(rowin)] for d in range(colin)]
new_list = list()

for row in range(rowin):
    for col in range(colin):
        my_list[row][col] = row * col

for i in my_list:
    print(i)

