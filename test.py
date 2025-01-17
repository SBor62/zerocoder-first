# Банк

def bank(a, years):
    for _ in range(years):
        a += a * 0.10  # Увеличиваем вклад на 10%

    return a

# Ввод данных
deposit = float(input("Введите сумму вклада: "))
num_years = int(input("Введите срок вклада в годах: "))

result = bank(deposit, num_years)

print(f"Сумма на счету через {num_years} лет: {result} ")