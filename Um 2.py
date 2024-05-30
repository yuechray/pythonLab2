def sum_list(lst):
    total = 0
    for item in lst:
        try:
            total += float(item)
        except ValueError:
            print(f"Невозможно преобразовать '{item}' в число")
    return total

# Ввод данных от пользователя
num_elements = int(input("Введите количество элементов в списке: "))
elements_list = []

for _ in range(num_elements):
    element = input("Введите элемент: ")
    elements_list.append(element)

# Вывод результата
result = sum_list(elements_list)
print("Сумма элементов:", result)
