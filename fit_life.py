""" Проект FitLife - MVP версия 1.0 """

def fitlife():
    """Знакомство, приведение имени к правильному формату """
    print('Привет! Я бот FitLife. Давай знакомиться.')
    user_name = input('Как тебя зовут?')
    name_formated = user_name.capitalize()

    # Ввод возраста, веса и роста, с проверкой
    try:
        user_age = int(input('Сколько тебе лет? '))
        user_weight = float(input('Введи свой вес (в кг): '))
        user_height = float(input('Введи свой рост (в метрах, например 1.70):'))
    except ValueError:
        print('Ошибка: пожалуйста, вводите числа для возраста, веса и роста.')
        return

    # Расчет ИМТ и нормы потребления воды с округлением результата
    if user_height <= 0:
        print('Рост должен быть больше нуля.')
        return
    bmi = round(user_weight / (user_height ** 2), 1)
    norm_water = round((user_weight * 0.03), 1)

    # Вывод отчета
    print("\n" + "=" * 50)
    print(f'\nОтчёт для пользователя: {name_formated} ({user_age} лет)')
    print(f'Твой индекс массы тела (ИМТ): {bmi}')
    print(f'Рекомендуемая норма воды: {norm_water} л в день')
    print('\nРасчёт окончен. Будьте здоровы!')
    print("=" * 50)

# Вызов функции
fitlife()