def testing(num):
    if num == "":
        return "Empty string is not applicable"
    elif len(num) < 2 or len(num) > 32 ** 2 - 1:
        return "Incorrect line length"
    elif num.isdigit() or num[0] == "+" or num[0] == "-":
        return int(num)
    else:
        return "Invalid input format"
