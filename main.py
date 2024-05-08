def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

def sort_list(arr):
    return sorted(arr)

# Ввод последовательности чисел
input_sequence = input("Введите последовательность чисел через пробел: ")
try:
    numbers = list(map(int, input_sequence.split()))
except ValueError:
    print("Ошибка: В последовательности должны быть только числа.")
    exit()

# Сортировка списка
sorted_numbers = sort_list(numbers)

# Ввод числа от пользователя
user_number = input("Введите любое число: ")
try:
    user_number = int(user_number)
except ValueError:
    print("Ошибка: Введено не число.")
    exit()

# Поиск позиции элемента
position = binary_search(sorted_numbers, user_number)

if position == len(sorted_numbers):
    print(f"Число {user_number} больше всех чисел в последовательности.")
else:
    print(f"Позиция числа {user_number} в отсортированной последовательности: {position}")

