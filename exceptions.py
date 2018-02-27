def ask_user():
    while True:
        try:
            user_question = input('Задайте вопрос или введите \'Пока!\' для выхода: ')
            answer = get_answer(user_question)
            print(answer)

            if user_question =='Пока!':
                break

        except KeyboardInterrupt:
            print('\nПока!')
            break


def get_answer(question):
    return(question)

if __name__ == "__main__":
    ask_user()