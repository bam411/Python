# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

def prime(n):
    i = 2
    flag = True
    while i < n // 2 + 1 and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return "yes"
    return "no"


print(prime(int(input())))
