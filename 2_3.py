my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # Исходный список
i = 0  # Индекс для перебора элементов списка

while i < len(my_list):
    number = my_list[i]
    if number < 0:  # Если встречается отрицательное число
        break  # Прерываем цикл
    elif number > 0:  # Если число положительное
        print(number)  # Выводим его
    i += 1  # Увеличиваем индекс для перехода к следующему элементу