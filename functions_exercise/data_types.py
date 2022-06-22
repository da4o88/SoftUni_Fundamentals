data_type = input()
data = input()


def multiple_by_data_int(number):
    return number * 2


def multiple_by_data_real(number):
    number = number * 1.5
    number_rounded = ('%.2f' %number)
    return number_rounded


def data_string_add_symbol(word):
    word = '$' + word + '$'
    return word


if data_type == 'int':
    result = multiple_by_data_int(int(data))
elif data_type == 'real':
    result = multiple_by_data_real(float(data))
elif data_type == 'string':
    result = data_string_add_symbol(data)

print(result)
