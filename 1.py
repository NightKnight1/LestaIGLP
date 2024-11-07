def isEven_1(value):
    """
    Плюсы: Легко понять, как работает функция.
    Минусы: Не самая большая скорость выполнения.
    """
    return value % 2 == 0

def isEven_2(value):
    """
    Плюсы: Большая скорость выполнения.
    Минусы: Может быть не сразу понятно, как работает функция.
    """
    return value & 1 == 0
