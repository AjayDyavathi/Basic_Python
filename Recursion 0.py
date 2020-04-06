def pretty_print_num(num):
    if num < 10:
        print(num)

    else:
        print(num)
        pretty_print_num(num//10)
        print(num)


def len_string(string):
    if string:
        return 1 + len_string(string[1:])
    else:
        return 0

    
def reverse(str):
    if str == '':
        return str
    else:
        return reverse(str[1:]) + str[0]
    
def dig_sum(num):
    num = str(num)
    if num:
        return num[0]+dig_sum(num[1:])
    else:
        return '0'
