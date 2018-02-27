list_users = ['Вася', 'Маша', 'Петя', 'Петя', 'Валера', 'Саша', 'Даша']

user_name = ''

while not user_name == 'Валера':
    print(list_users)
    user_name = list_users.pop()

print('Валера нашелся')