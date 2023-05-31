def calculate_bmr(weight, height, age, gender):
    """
    Расчет базового обмена веществ (BMR) по формуле Харриса-Бенедикта.
    :param weight: вес в кг
    :param height: рост в см
    :param age: возраст в годах
    :param gender: пол (0 - женский, 1 - мужской)
    :return: BMR в калориях
    """
    if gender == 0:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif gender == 1:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        raise ValueError("Неправильное значение параметра gender. Должно быть 0 (женский) или 1 (мужской).")
    return bmr


def calculate_tdee(bmr, activity_level):
    """
    Расчет общей энергозатраты на основе базового обмена веществ (BMR) и уровня физической активности.
    :param bmr: базовый обмен веществ в калориях
    :param activity_level: уровень физической активности (1.2 - сидячий образ жизни, 1.375 - низкая активность,
                           1.55 - средняя активность, 1.725 - высокая активность, 1.9 - очень высокая активность)
    :return: TDEE в калориях
    """
    tdee = bmr * activity_level
    return tdee


def calculate_calories_for_weight_loss(tdee, weight_loss_per_week):
    """
    Расчет количества калорий, необходимых для похудения на заданное количество килограммов в неделю.
    :param tdee: общая энергозатрата в калориях
    :param weight_loss_per_week: желаемая потеря веса в кг в неделю
    :return: количество калорий, необходимых для похудения
    """
    calories_for_weight_loss = tdee - (weight_loss_per_week * 7700 / 7)
    return calories_for_weight_loss


# Пример использования функций для расчета калорий для похудения
weight =