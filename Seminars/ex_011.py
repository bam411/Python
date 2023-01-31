# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input:   5
# Output:  6

n = int(input('Введите число: '))
a0 = 0
a1 = 1
count = 1
while a0 < n:
    x = a0 + a1
    a0 = a1
    a1 = x
    count += 1
if a0 != n:
    print(-1)
else:
    print(count)