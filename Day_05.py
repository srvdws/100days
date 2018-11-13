# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class GetAndPrintString():

    def __init__(self):
        self.string = ""

    def getstring(self):
        self.string = input("a string plz: ")

    def printstring(self):
        print(self.string.upper())

my_getter_printer = GetAndPrintString()


my_getter_printer.getstring()
my_getter_printer.printstring()

