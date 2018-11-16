# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class GetAndPrint():

    def __init__(self):
        self.str = ""

    def getter(self):
        self.str = input('str plz: ')

    def printer(self):
        print(self.str.upper())


my_str = GetAndPrint()

my_str.getter()
my_str.printer()




# class StringGetterPrinter():
#
#     def __init__(self):
#         self.string = ""
#
#     def getstring(self):
#         self.string = input("enter a string: ")
#
#     def printstring(self):
#         print(self.string)
#
#
# my_printer_getter = StringGetterPrinter()
# my_printer_getter.getstring()
# my_printer_getter.printstring()
