# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
count = 0
multiply = 0
number = 6
lst = []
while count < number:
    for i in range(1, number+1):
        multiply = (1+(1/i))**i
        lst.append(round(multiply, 2))
        count += 1

print(lst)
print(f'The sum of numbers in the list is : ', sum(lst))
