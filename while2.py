list_users = ['Вася', 'Маша', 'Петя', 'Петя', 'Валера', 'Саша', 'Даша']


def find_person(name):
    
    user_name = ''

    while not user_name == name:
        print(list_users)

        if len(list_users) == 0:
            print('Мы не нашли пользователя с именем {}'.format(name))
            break

        user_name = list_users.pop()

        if user_name == name:
            print('Мы нашли пользователя с именем {}'.format(name))

    return user_name

person = find_person('Маша')
