pets = ["dog", "cat", "bird", "rabbit", "fish", "neigbour"]

# to get each item in list printed I could...

for i in pets:
    print(i)

# rock out a conditional statement with a while loop

i_got_20 = 20

while i_got_20 < 35:
    print(i_got_20)
    i_got_20 += 1
print("gimme money")

# x = 5
# while x > 3: # make this conditional true for infinte loop
#   print("This is dumb, don't uncomment")

# for all numbers between 1500 and 2700, which are divisible by 7 and a multiple of 5

for i in range(1500, 2701):
    if not i % 7 and not i % 5:
        print(i)

