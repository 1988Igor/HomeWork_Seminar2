# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

count = 0
multiply = 1
number = 4
lst = []
while count < number:
    for i in range(1, number + 1):
        multiply *= i
        lst.append(multiply)
        count += 1
    print(f'The sum of product of numbers from 1 to N is :\n {lst}')
