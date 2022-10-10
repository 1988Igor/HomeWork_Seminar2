# Реализуйте алгоритм перемешивания списка.
from random import shuffle
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'The first list {lst}')
lst2 = []
lst2 = lst
shuffle(lst2)
print(f'The changed list {lst2}')