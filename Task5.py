# Реализуйте алгоритм перемешивания списка.

import random
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'The first list {lst}')
lst2 = []
lst2 = lst
random.shuffle(lst2)
print(f'The shuffled list {lst2}')
