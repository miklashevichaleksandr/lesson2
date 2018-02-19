def strings_comparsion(str_one, str_two):
    if str_one == str_two:
        return '1'
    else:
        if len(str_one) > len(str_two):
            return '2'
        elif str_two == 'learn':
            return '3'

result1 = strings_comparsion('short', 'short')
print(result1)

result2 = strings_comparsion('loooooooong', 'short')
print(result2)

result3 = strings_comparsion('short', 'learn')
print(result3)