""" Модуль для генерации объектов типа Сar
  ФИО владельца, марка, год выпуска, гос. номер, цвет
  (сравнение по полям – гос. номер, год выпуска, марка, цвет, ФИО владельца)"""

from russian_names import RussianNames  # RussianNames имеет метод get_person(), возвращающий ФИО
import random
# Список возможных моделей
model = ["LADA", "Volga", "Dodge", "Chrysler", "Acura", "Audi","Bentley", "BMW", "Cadillac", "Chery", "Citroen","Peugeot","Daewoo ",
            "FIAT", "FORD", "Honda", "Hyundai", "HUMMER", "Infiniti", "Jaguar", "Jeep", "Kia", "Lexus", "LIFAN", "Mazda", "Mercedes-Benz",
            "Volvo", "UAZ", "Toyota", "Suzuki", "Subaru", "SsangYong", "Skoda", "SAAB", "Renault", "Pontiac", "Porsche", "Opel", "Nissan",
            "Mitsubishi"]

#Список возможных цветов
col=["Черный", "Абрикосовый", "Розовый","Арлекин","Бежевый", "Белый", "Бирюзовый", "Синий", "Бурый", "Зеленый", "Желтый","Красный"]

def car_number():
    """ Функция возвращающая сл. номер авто"""
    b = ["А", "В", "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
    k1 = random.randint(0, 11)
    k2 = random.randint(0, 11)
    k3 = random.randint(0, 11)
    g1 = random.randint(0, 9)
    g2 = random.randint(0, 9)
    g3 = random.randint(0, 9)
    g4 = random.randint(0, 9)
    g5 = random.randint(0, 9)
    a = b[k1] + str(g1) + str(g2) + str(g3) + b[k2] + b[k3] + str(g4) + str(g5)
    return a


def generation(n):
    """ Генерирует словарь длины n с перечисленными полями:
    ФИО, марка, год выпуска, гос. номер, цвет."""
    dictionary = {}
    full_name = []  # ФИО
    models = []  # модель
    year = []  # год выпуска
    number = []  # номер авто
    color=[] #цвет
    for i in range(n):
        full_name.append(RussianNames().get_person())
        models.append(model[random.randrange(0, (len(model)-1))])
        year.append(random.randint(1986, 2023))
        number.append(car_number())
        color.append(col[random.randrange(0, 11)])
    dictionary['ФИО'] = full_name
    dictionary['Модель'] = models
    dictionary['Год выпуска'] = year
    dictionary['Гос. номер'] = number
    dictionary['Цвет'] = color
    return dictionary