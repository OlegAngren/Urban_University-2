def ancient_cipher(n):
    result = ""
    # Перебираем все числа от 1 до n-1
    for i in range(1, n):
        for j in range(i + 1, n):
            # Проверяем, кратна ли сумма пары n
            if n % (i + j) == 0:
                result += f"{i}{j}"
    return result

# Пример использования:
n = int(input("Введите число от 3 до 20: "))
print("Нужный пароль:", ancient_cipher(n))