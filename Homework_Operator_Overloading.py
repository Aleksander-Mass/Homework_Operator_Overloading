
'''

Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса":

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"



Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.
'''



class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Метод сравнения на равенство
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    # Метод сравнения <
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    # Метод сравнения <=
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    # Метод сравнения >
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    # Метод сравнения >=
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Метод сравнения !=
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    # Метод для сложения (увеличения этажей)
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Метод для правостороннего сложения
    def __radd__(self, value):
        return self.__add__(value)

    # Метод для +=
    def __iadd__(self, value):
        return self.__add__(value)


# Пример использования:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# Сравнение на равенство
print(h1 == h2)  # False

# Увеличение этажей с помощью __add__
h1 = h1 + 10
print(h1)  # Теперь у h1 20 этажей
print(h1 == h2)  # True

# Использование += (__iadd__)
h1 += 10
print(h1)  # Теперь у h1 30 этажей

# Использование правостороннего сложения (__radd__)
h2 = 10 + h2
print(h2)  # Теперь у h2 30 этажей

# Другие операторы сравнения
print(h1 > h2)   # False
print(h1 >= h2)  # True
print(h1 < h2)   # False
print(h1 <= h2)  # True
print(h1 != h2)  # False

'''
Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
'''