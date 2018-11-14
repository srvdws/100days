# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class StringGetterPrinter():

    def __init__(self):
        self.string = ""

    def getstring(self):
        self.string = input("enter a string: ")

    def printstring(self):
        print(self.string)


my_printer_getter = StringGetterPrinter()
my_printer_getter.getstring()
my_printer_getter.printstring()
