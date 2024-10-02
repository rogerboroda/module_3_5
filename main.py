def get_multiplied_digits(number):
    str_number = str(number)  # number  в строку
    first = int(str_number[0]) # Первое число в number
    if number == 0:
        return 1
    if 1 < len(str_number) or int(str_number[-1]) != 0:  # если меньше одного
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(402030)
print(result)