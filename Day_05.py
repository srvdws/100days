# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase

class StringGetterAndPrinter():

    def __init__(self):
        self.string = ""

    def getstring(self):
        self.string = input("Enter a string: \n")

    def printstring(self):
        print(self.string.upper())

mystring = StringGetterAndPrinter()

mystring.getstring()

mystring.printstring()

