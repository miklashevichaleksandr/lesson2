user_age = input('Введите ваш возраст: ')
user_age = int(user_age)

if user_age <= 6:
    print ('Вам нужно учиться в детском саду')
elif 6 < user_age <= 17:
    print('Вам нужно учиться в школе')
elif 17 < user_age <= 23:
    print('Вам нужно учиться в ВУЗе')
elif user_age > 23:
    print('Вам нужно работать')