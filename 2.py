from collections import deque


class CircularBuffer_1():
    """
    Плюсы:  Реализация с использованием встроенного контейнера (list).
            Эффективный по скорости выполнения (add), т.к. list имеет заранее определенный
            размер(не будет случаев его перемещения в памяти при добавлении новых данных, пока буфер не полный)
    Минусы: Когда буфер не полный, "show" выводит 'None' для еще не занятых ячеек памяти (это можно исправить дополнительно реализовав внутри класс для полного буфера).
    """

    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.index = 0

    def add(self, val):
        self.data[self.index] = val
        self.index = (self.index + 1) % self.size

    def show(self):
        print(self.data[self.index:] + self.data[:self.index])


class CircularBuffer_2():
    """
    Плюсы:  Использование структуры данных, реализованных другим программистом (не нужно "изобретать велосипед").
    Минусы: Использование структуры данных, реализованных другим программистом (необходимость понимания реализации). Также, используется лишь часть функционала deque.
    """

    def __init__(self, size):
        self.size = size
        self.data = deque(maxlen=size)

    def add(self, val):
        self.data.append(val)

    def show(self):
        print(list(self.data))
