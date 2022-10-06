from list_28_07 import*
tuple_ = ('one', 'two', False, 2)
print(type(tuple_))
print(id(tuple_))
###################
tuple_2 = 'one', 'two', 2, 3, False #Другий спосід створення кортежу
print(type(tuple_2))
print(id(tuple_2))
###################
a, b, c = 'one', 'two', 'three'# Кортеж дозволяє присвоїти декілька змінних за раз
print(a,b,c)
###################
transform_to_tuple = tuple(list_)
print(transform_to_tuple)