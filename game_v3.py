import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    lower_bound = 1
    upper_bound = 100

    while True:
        count += 1
        # Предполагаемое число - это среднее значение текущего диапазона
        predict_number = (lower_bound + upper_bound) // 2
        
        if number == predict_number:
            break  # выходим из цикла, если угадали
        elif number < predict_number:
            upper_bound = predict_number - 1  # обновляем верхнюю границу
        else:
            lower_bound = predict_number + 1  # обновляем нижнюю границу

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
score_game(binary_predict)