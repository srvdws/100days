# reverse an input string

x = input("enter string to reverse: ")
print(x[::-1])

# count even or odd from a series of numbers:
testlist = [1,2,3,4,5,6,7,8,9,10,11]


def odder_evener(li):

    odds = [i for i in li if i % 2 != 0]
    evens = [i for i in li if i % 2 == 0]

    return "\nodds: " + str(len(odds)) + "\nevens: " + str(len(evens))


print(odder_evener(testlist))



