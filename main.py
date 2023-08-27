Задача 10
import random
n = int(input("Введите количество монеток (n): "))
coins = list(range(n)) 
random.shuffle(coins) 
flips = 0 
while any(coin == 0 for coin in coins): # пока не все монеты лежат одной стороной
 coin = coins.pop(0) 
 flips += 1 
print(f"Минимальное количество перевернутых монеток: {flips}")

Задача 12
def find_numbers(s, p):
    for x in range(1, 1001):
        y = s - x
        if x * y == p:
            return x, y

sum_hint = int(input("Введите сумму чисел: "))
product_hint = int(input("Введите произведение чисел: "))

result = find_numbers(sum_hint, product_hint)

if result:
    print(f"Задуманные числа Петей: {result[0]} и {result[1]}")
else:
    print("Не удалось найти числа, соответствующие подсказкам.")

Задача 14
def powers_of_two(n):
    powers = []
    k = 0
    power = 1

    while power <= n:
        powers.append(power)
        k += 1
        power = 2 ** k

    return powers

number = int(input("Введите число N: "))

result = powers_of_two(number)

print("Целые степени двойки, не превосходящие", number, ":")
for num in result:
    print(num)