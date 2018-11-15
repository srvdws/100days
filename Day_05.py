# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class GetterAndPrinter():

    def __int__(self):
        self.s = ""

    def getter(self):
        self.s = input("str pls: ")

    def printer(self):
        print(self.s.upper())


mystring = GetterAndPrinter()

mystring.getter()
mystring.printer()





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
