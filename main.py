class NumberFormatter:

    def parseInt(self, string):
        if string == "":
            return "Empty string is not applicable"
        elif len(string) < 2 or len(string) > 32 ** 2 - 1:
            return "Incorrect line length"
        elif string.isdigit() or string[0] == "+" or string[0] == "-":
            return int(string)
        else:
            return "Invalid input format"


my_object = NumberFormatter()
print(my_object.parseInt(""))
