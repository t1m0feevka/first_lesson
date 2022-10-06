list_ = ['1', '2', '3']
print(type(list_))
print(id(list_))

list_2 = ['Monday', 'Friday', 25, 18, False, True, [17, 'Sunday'], 'cat']
print(list_2[6][0])
list_2[0] = 1 #заміна елемента під індексом 0 на 1
print(list_2[1:3]) #зріз
list_2.append('dog') #додає елемент в кінець списку
list_2.pop(3)  # видалення елементу під індексом 3
list_2.remove(25) # видалення елементу під значенням 25
list_2.insert(5, 'home') # додавання елементу "home" під індекс 5
print(list_2.index('cat')) #Визначити індекс елементу
list_2.extend(list_) #додає один список до іншого як елементи
list_2.reverse() #відображає дзеркально всі елементи
list_2.sort() #сортує всі елементи по алфавіту або від меншого до більшого
print('cat' in list_2) #перевірка наявності елемента в списку
print(list_2.count('cat'))#виводить кількість елементів під значенням 'cat'
all_list2 = ',-'.join(list_) #додає ,- після кожного елемента
print(all_list2)
print(list_2)
