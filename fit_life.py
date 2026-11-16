"""Проект FitLife - MVP версия 1.0"""

# Константы
WATER_COEFFICIENT = 0.03          # норма воды: X литров на 1 кг веса



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
    try:
        user_age = int(input('Сколько тебе лет? '))
    except ValueError:
        print('Ошибка: возраст должен быть целым числом.')
        return

    try:
        user_weight = float(input('Введи свой вес (в кг): '))
    except ValueError:
        print('Ошибка: вес должен быть числом.')
        return
    try:
        user_height = float(
            input('Введи свой рост (в метрах, например 1.70): ')
        )
    except ValueError:
        print('Ошибка: рост должен быть числом.')
        return

    # Расчет ИМТ и нормы потребления воды с округлением результата
    if user_height <= 0:
        print('Рост должен быть больше нуля.')
        return
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
