# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class MyGetterPrinter():

    def __init__(self):
        self.s = ""

    def getter(self):
        self.s = input("feed me strings: ")

    def printer(self):
        return self.s.upper()


my_string = MyGetterPrinter()

my_string.getter()
print(my_string.printer())


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
