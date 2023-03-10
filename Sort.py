"""Модуль с реализованными сортировками:
Сортировка выбором, быстрая сортировка, слиянием"""



def sel_sort(array):
    """Функция сортировки выбором"""
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
    return array

def quick_sort(data, start, end):
    """
    Функция быстрой сортировки
    Параметры:
    data ( list(Partner) ) : массив данных для сортировки
    start ( int ) : левая граница разбиения
    end ( int ) : правая границы разбиения
    Возвращаемые значения:
    отсутствуют: функция принимает массив и изменяет его
    """
    def partition(data, start, end): # определяем опорный элемент и границы разбиения
        pivot = data[start]
        l = start + 1
        r = end
        # проходимся по отрезку и сравниваем с опорным
        while True:
            while l <= r and data[r] >= pivot:
                r -= 1
            while l <= r and data[l] <= pivot:
                l += 1
            if l <= r:
                data[l], data[r] = data[r], data[l]
            else:
                break
        data[start], data[r] = data[r], data[start]
        return r
    if start >= end:
        return
    # разбиваем массив и сортируем
    p = partition(data, start, end)
    quick_sort(data, start, p-1)
    quick_sort(data, p+1, end)
    return


def merge(arr, low, mid, high):
    """ Функция для записи отсортированного подмассива в оригинальный массив"""
    buffer = [None] * (high + 1 - low)
    h, i, j = low, 0, mid + 1

    while h <= mid and j <= high:
        if arr[h] <= arr[j]:
            buffer[i] = arr[h]
            h += 1
        else:
            buffer[i] = arr[j]
            j += 1
        i += 1

    if h > mid:
        for k in range(j, high + 1):
            buffer[i] = arr[k]
            i += 1
    else:
        for k in range(h, mid + 1):
            buffer[i] = arr[k]
            i += 1

    for k in range(0, high - low + 1):
        arr[low + k] = buffer[k]


def merge_sort(arr, low, high):
    """ Сортирует массив сортировкой слиянием"""
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)