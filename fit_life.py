"""Проект FitLife - MVP версия 1.0"""

# Константы
WATER_COEFFICIENT = 0.03          # норма воды: X литров на 1 кг веса
MIN_AGE = 1
MAX_AGE = 120
MIN_WEIGHT = 30
MIN_HEIGHT = 0.5


def read_float(prompt: str) -> float:
    """Запрашивает у пользователя число с плавающей точкой.
    Повторяет ввод при ошибке.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Ошибка: нужно ввести число. Попробуйте ещё раз.')


def process_user_fitness():
    """Знакомство, приведение имени к правильному формату."""
    print('Привет! Я бот FitLife. Давай знакомиться.')
    user_name = input('Как тебя зовут?')
    user_name = user_name.capitalize()

    # Ввод возраста, веса и роста, с проверкой
    while True:
        age = read_float('Сколько тебе лет? ')
        if MIN_AGE <= age <= MAX_AGE:
            user_age = int(age)
            break
        print(f'Ошибка: возраст должен быть от {MIN_AGE} до {MAX_AGE}.')

    while True:
        user_weight = read_float('Введи свой вес (в кг): ')
        if user_weight >= MIN_WEIGHT:
            break
        print(f'Ошибка: вес должен быть не меньше {MIN_WEIGHT} кг.')

    while True:
        user_height = read_float('Введи свой рост (в метрах, например 1.70): ')
        if user_height >= MIN_HEIGHT:
            break
        print(f'Ошибка: рост должен быть не меньше {MIN_HEIGHT} м.')

    # Расчет ИМТ и нормы потребления воды с округлением результата
    bmi = round(user_weight / (user_height ** 2), 1)
    norm_water = round((user_weight * WATER_COEFFICIENT), 1)

    # Вывод отчета пользователю
    print("\n" + "=" * 50)
    print(f'\nОтчёт для пользователя: {user_name} ({user_age} лет)')
    print(f'Твой индекс массы тела (ИМТ): {bmi}')
    print(f'Рекомендуемая норма воды: {norm_water} л в день')
    print('\nРасчёт окончен. Будьте здоровы!')
    print("=" * 50)


# Вызов функции
if __name__ == '__main__':
    process_user_fitness()
