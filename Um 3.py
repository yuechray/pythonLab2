def max_value(lst):
    if not lst:
        return None
    maximum = lst[0]
    for item in lst:
        if item > maximum:
            maximum = item
    return maximum

# Ввод данных от пользователя
num_elements = int(input("Введите количество элементов в списке: "))
elements_list = []

for _ in range(num_elements):
    element = input("Введите элемент: ")
    elements_list.append(element)

# Вывод результата
result = max_value(elements_list)
print("Максимальное значение:", result)
