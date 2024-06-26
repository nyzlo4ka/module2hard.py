def generate_password(n):
    password = ''
    for i in range(1, 21):
        for j in range(i+1, 21):
            if (i + j) <= 20 and n % (i + j) == 0:
                password += str(i) + str(j)
    return password


n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print("Пароль:", result)
