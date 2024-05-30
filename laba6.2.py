def f(x1, x2):
    # Задайте вашу функцію тут
    return x1 * x2  # приклад функції множення

def calculate_average(x1, x2):
    return (x1 + x2) / 2

x1 = float(input("Введіть x1: "))
x2 = float(input("Введіть x2: "))
variant_number = input("Введіть номер вашого варіанту: ")

# Переконайтеся, що номер варіанту дійсно введено і він є числом
if not variant_number.isdigit():
    print("Введіть коректний номер варіанту!")
else:
    variant_last_digit = int(variant_number[-1])

    result = f(x1, x2)

    if variant_last_digit in [0, 1, 2, 3]:
        average = calculate_average(x1, x2)
        print(f"Середнє арифметичне значень x1 та x2: {average}")
        print(f"Результат функції f(x1, x2): {result:.4f}")
    elif variant_last_digit in [4, 5, 6]:
        minimum = min(x1, x2)
        print(f"Менше значення з x1 та x2: {minimum}")
        print(f"Результат функції f(x1, x2): {result:.3f}")
    elif variant_last_digit in [7, 8, 9]:
        maximum = max(x1, x2)
        print(f"Більше значення з x1 та x2: {maximum}")
        print(f"Результат функції f(x1, x2): {result:.2e}")
    else:
        print("Невірна остання цифра варіанту!")
