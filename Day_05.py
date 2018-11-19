# Create a class that has two methods:
# getstring: take a string
# printstring: print a string in uppercase


class GetAndPrint():

    def __init__(self):
        self.str = ""

    def gets(self):
        self.str = input("Enter a string please: ")

    def prints(self):
        print(self.str.upper())


my_string = GetAndPrint()

my_string.gets()
my_string.prints()



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
