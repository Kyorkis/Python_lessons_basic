# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

#def fibonacci(n, m):
#    number = [1,1]
#    for i in range (2, n+1):
#        number.append(number[-1]+number[-2])
#        return number
#        print (fibonacci(5,10))


#def fibonacci(n, m):
   
#    a, b = 1, 1
#   f_list = [1, ]
 
#    for i in range(m):
#        a, b = b, a + b
#        f_list.append(a)
 
#    return f_list[n - 1:m]
 
 
#print('fibonacci(1, 6): ', fibonacci(1, 6))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#def sort_to_max(origin_list):
#    if len(origin_list) > 1:
#        x = len(origin_list) // 2
#        small = []
#        large = []
 
#        for i, val in enumerate(origin_list):
#            if i != x:
#                if val < origin_list[x]:
#                    small.append(val)
#                else:
#                    large.append(val)
 
#        sort_to_max(small)
#        sort_to_max(large)
#        origin_list[:] = small + [origin_list[x]] + large
 
#    return origin_list
 
 
#print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#x = [11,121,-7,54,"Fdv", 9860,"Hello",11,-5]
#def filt(arg,obj):
#    print (obj)
#    x_1 = []
#    for i in obj :
#        if i != arg:
#            x_1.append(i)
#    print (x_1)
#filt(11,x)
            
#filt(4, z)
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.



