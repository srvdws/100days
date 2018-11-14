import math

# Create a cool calculator

c = 50
h = 30

# Use this formula: Q = square root of [(2 * c * d) / h]
# Input d as a list of values, calculate Q and output as a list/scv of ints


my_inputs = (i for i in input("yes? ").split(','))
print(list(my_inputs))
Q_list = list()
my_list = list(my_inputs)

for d in my_inputs:
    Q_list.append(int(math.sqrt(round((2 * c * int(d)) / h))))

print(Q_list)

# my_inputs = (i for i in input("enter a number: ").split(","))
# Q_list = list()
#
# for d in my_inputs:
#     Q_list.append(int(round(math.sqrt((2 * c * int(d)) / h))))
#
# print(Q_list)
