def raise_to_power(lst, power):
    result = []
    for item in lst:
        try:
            number = float(item)
            result.append(number ** power)
        except ValueError:
            result.append(item * power)
    return result

# Ввод данных от пользователя
num_elements = int(input("Введите количество элементов в списке: "))
elements_list = []

for _ in range(num_elements):
    element = input("Введите элемент (число или строку): ")
    elements_list.append(element)

power = int(input("Введите степень, в которую нужно возвести элементы: "))

# Вывод результата
result = raise_to_power(elements_list, power)
print("Результат:", result)

