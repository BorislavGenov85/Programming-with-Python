import random

questions = [
    'От кой език идва думата „пенкилер“?',
    'Коя европейска столица носи името на един от най-известните магистри от ордена на йоанитите?',
    'Изразът „желязна завеса“ добива популярност сред реч на Чърчил от 1946 г. Кои градове са в двата ѝ края?',
    'Министър с какъв ресор назначи бившият премиер Тереза Мей през 2018 г.?',
    'Коя забележителност ЮНЕСКО определя като единствена по рода си в Европа?'
]

questions_asked = []
guess_question_counter = 0
wrong_answer_counter = 0

while True:
    current_question = random.choice(questions)

    if current_question not in questions_asked:
        print(current_question)
        questions_asked.append(current_question)
    else:
        continue

    if current_question == 'От кой език идва думата „пенкилер“?':
        user_answer = input('Въведи орговор: ')

        if user_answer == 'Английски':
            print('Ти позна!\n')
            guess_question_counter += 1
        else:
            wrong_answer_counter += 1

    elif current_question == 'Коя европейска столица носи името на един от най-известните магистри от ордена на йоанитите?':
        user_answer = input('А. Дъблин\nВ. Валета\nС. Вадуц\nD. Мадрид\n\nВъведи орговор: ')

        if user_answer.lower() == 'b':
            print('Ти позна!\n')
            guess_question_counter += 1
        else:
            wrong_answer_counter += 1

    elif current_question == 'Изразът „желязна завеса“ добива популярност сред реч на Чърчил от 1946 г. Кои градове са в двата ѝ края?':
        user_answer = input('Въведи орговор: ')

        if user_answer == 'Шчечин и Триест':
            print('Ти позна!\n')
            guess_question_counter += 1
        else:
            wrong_answer_counter += 1

    elif current_question == 'Министър с какъв ресор назначи бившият премиер Тереза Мей през 2018 г.?':
        user_answer = input('Въведи орговор: ')

        if user_answer == 'Самота':
            print('Ти позна!\n')
            guess_question_counter += 1
        else:
            wrong_answer_counter += 1

    elif current_question == 'Коя забележителност ЮНЕСКО определя като единствена по рода си в Европа?':
        user_answer = input('Въведи орговор: ')

        if user_answer == 'Мадарският конник':
            print('Ти позна!\n')
            guess_question_counter += 1
        else:
            wrong_answer_counter += 1

    if guess_question_counter == 3:
        print('>>>>> Ти спечели играта <<<<<\nПечелиш голямата награда!')
        break

    elif wrong_answer_counter == 2:
        print('....Ти загуби играта....\nОпитай отново!')
        break
