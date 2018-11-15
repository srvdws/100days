import math

# Create a cool calculator

c = 50
h = 30

# Use this formula: Q = square root of [(2 * c * d) / h]
# Input d as a list of values, calculate Q and output as a list/scv of ints
# test string = 6,8,10


my_input = [i for i in input("::").split(",")]
q_list = list()

for d in my_input:
    q_list.append(int(math.sqrt(round((2 * c * int(d)) / h))))


print(q_list)

