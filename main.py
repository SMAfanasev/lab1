"""В данном модуле генерируем наборы данных различной размерности.
Далее записываем их в .xlsx. Затем считываем их из файла, сортируем и
сохраняем в новых файлах. С помощью таймера засекаем время работы функций сортировок."""

import copy
import time
import pandas as pd
from Car import Car
from Generation import generation
from Sort import sel_sort
from Sort import merge_sort
from Sort import quick_sort

# размерности наборов данных для генерации
size = [100, 200, 400, 700, 1000, 1500, 5000]

# Запись сгенерированных файлов в файл
with pd.ExcelWriter("./Cars.xlsx") as writer:
    for i in size:
        pd.DataFrame(generation(i)).to_excel(writer, sheet_name=f"{i}", index=False)

# Чтение из файла и запись в словарь, для дальнейшей сортировки
cars = {}
for i in size:
    c = pd.read_excel('./Cars.xlsx', sheet_name=f'{i}').to_dict('records')
    c_cars = []
    for empl in c:
        c_cars.append(
            Car(empl['ФИО'], empl['Модель'], empl['Год выпуска'], empl['Гос. номер'], empl['Цвет']))
    cars[i] = c_cars

#списки для хранения времени, потраченного на сортировку
time_sel_sort = []
time_merge = []
time_quick = []

#сортировка данных, считанных из файла .xlsx
for j in size:
    sorted_arrays = []

    #сортировка выбором
    sorted_arr_sel_sort = copy.deepcopy(cars[j])
    start = time.time()
    sel_sort(sorted_arr_sel_sort)
    end = time.time()
    time_sel_sort.append(end - start)
    sorted_arrays.append(sorted_arr_sel_sort)

    #сортировка слиянием
    sorted_arr_merge = copy.deepcopy(cars[j])
    start = time.time()
    merge_sort(sorted_arr_merge, 0, len(sorted_arr_merge) - 1)
    end = time.time()
    time_merge.append(end - start)
    sorted_arrays.append(sorted_arr_merge)

    #быстрая сортировка
    sorted_arr_quick = copy.deepcopy(cars[j])
    start = time.time()
    quick_sort(sorted_arr_quick, 0, len(sorted_arr_quick) - 1)
    end = time.time()
    time_quick.append(end - start)
    sorted_arrays.append(sorted_arr_quick)

    for i in range(len(sorted_arrays)):
        dictionary = {}
        full_name = []
        model = []
        year = []
        number = []
        color = []

        for k in sorted_arrays[i]:
            full_name.append(k.name)
            model.append(k.mod)
            year.append(k.year)
            number.append(k.num)
            color.append(k.col)
        dictionary['ФИО'] = full_name
        dictionary['Марка'] = model
        dictionary['Год выпуска'] = year
        dictionary['Гос. номер'] = number
        dictionary['Цвет'] = color

        #записываем в разные файлы
        if i == 0:
            file_name = "./Cars_sorted_sel.xlsx"
        elif i == 1:
            file_name = "./Cars_sorted_merge.xlsx"
        else:
            file_name = "./Cars_sorted_quick.xlsx"

        #необходимо создать новый файл, если набор данных первый
         #иначе - дописываем (будут созданы новые листы excel)
        if j == size[0]:
            mode = 'w'
        else:
            mode = 'a'
        with pd.ExcelWriter(file_name, engine="openpyxl", mode=mode) as writer:
            pd.DataFrame(dictionary).to_excel(writer, sheet_name=f"{j}", index=False)

print(f'merge_time = {time_merge}')
print(f'sel_time = {time_sel_sort}')
print(f'quick_time = {time_quick}')
