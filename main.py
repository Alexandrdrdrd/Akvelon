class NumberFormatter():
    def __init__(self, string) :
        self.string=string
    
    def parseInt(self):
        if self.string == "":
            return "Empty string is not applicable"
        elif len(self.string) < 2 or len(self.string) > 32 ** 2 - 1:
            return "Incorrect line length"
        elif self.string.isdigit() or self.string[0] == "+" or self.string[0] == "-":
            return int(self.string)
        else:
            return "Invalid input format"



my_object = NumberFormatter("123")
print(my_object.parseInt())