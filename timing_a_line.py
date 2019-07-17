from timeit import timeit
print(timeit("my_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])"))
print(timeit("my_set = {*[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]}"))
