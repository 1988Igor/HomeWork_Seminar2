# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

count = 0
multiply = 0
number = int(input('Enter a number: '))
dictionary_ = {}
while count < number:
    for i in range(1, number+1):
        dictionary_[i] = (1+(1/i))**i
        count += 1
round_ = 2
for elem in dictionary_:
    dictionary_[elem] = round(dictionary_[elem], 2)
print(dictionary_)
print(f'The sum of numbers in the dictionary:', sum(dictionary_.values()))
