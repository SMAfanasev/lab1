class Car:
    """ Класс, описывающий владельца"""

    def __init__(self, name, mod, year, num, col):
        """ Инициализация объекта"""
        self.name = name  # ФИО
        self.mod = mod  # модель
        self.year = year  # год выпуска
        self.num = num  # номер авто
        self.col = col  # Цвет

    def __lt__(self, other):
        """ Cравниваем поля в следующем порядке: гос. номер, год выпуска, марка, цвет, ФИО владельца
             Перегрузка оператора <"""
        if self.num != other.num:
            return self.num < other.num
        if self.year != other.year:
            return self.year < other.year
        if self.mod != other.mod:
            return self.mod < other.mod
        if self.col != other.col:
            return self.col < other.col
        return self.name < other.name

    def __le__(self, other):
        """ Перегрузка оператора <="""
        if self.num != other.num:
            return self.num < other.num
        if self.year != other.year:
            return self.year < other.year
        if self.mod != other.mod:
            return self.mod < other.mod
        if self.col != other.col:
            return self.col < other.col
        return self.name <= other.name

    def __gt__(self, other):
        """ Перегрузка оператора >"""
        if self.num != other.num:
            return self.num > other.num
        if self.year != other.year:
            return self.year > other.year
        if self.mod != other.mod:
            return self.mod > other.mod
        if self.col != other.col:
            return self.col > other.col
        return self.name > other.name

    def __ge__(self, other):
        """ Перегрузка оператора >="""
        if self.num != other.num:
            return self.num > other.num
        if self.year != other.year:
            return self.year > other.year
        if self.mod != other.mod:
            return self.mod > other.mod
        if self.col != other.col:
            return self.col > other.col
        return self.name >= other.name

    def __eq__(self, other):
        """ Перегрузка оператора == """
        return (self.num == other.num and self.year == other.year 
                and self.mod == other.mod and self.col == other.col and self.name == other.name)