def ask_user():
    while True:
        user_question = input('Задайте вопрос или введите \'Пока!\' для выхода: ')
        answer = get_answer(user_question)
        print(answer)

        if user_question =='Пока!':
            break

def get_answer(question):
    return(question)

ask_user()