# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.56 -> 11

number = float(input('Enter a number :'))
str1 = str(number)
str2 = str1.replace('.', '')
my_number = int(str2)
remainder_ = 0
summ = 0
while (my_number != 0):
    remainder_ = my_number % 10
    summ = summ + remainder_
    my_number = my_number//10
print(summ)

