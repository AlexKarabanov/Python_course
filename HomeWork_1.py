# Задача 2: Найдите сумму цифр трехзначного числа.

# a = int (input ('Введите 3-значное число: '))

# print (a % 10 + a % 100 // 10 + a // 100)


# Задача 4: Петя, Катя и Сережа делают из бумаги 
# журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала 
# в два раза больше журавликов, чем Петя и 
# Сережа вместе?


# S = int (input ('S журавликов сделано: '))

# a = S / 6 

# if S % 6 == 0 :
#     print (4 * a, 'столько журавликов сделала Катя', a, 'по столько журавликов сделали Петя и Сережа')
# else :
#     print ('Они не могли сделать столько журавликов')



# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с 
# номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая 
# проверяет счастливость билета.


# a = int (input ('Введите 1-ю цифру: '))
# b = int (input ('Введите 2-ю цифру: '))
# c = int (input ('Введите 3-ю цифру: '))
# d = int (input ('Введите 4-ю цифру: '))
# e = int (input ('Введите 5-ю цифру: '))
# f = int (input ('Введите 6-ю цифру: '))


# if (a + b + c == d + e + f) :
#     print ('YES')
# else :
#     print ('NO')


# Задача 8: Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть 
# разломить шоколадку на два прямоугольника).

# n = int (input ('Введите n: '))
# m = int (input ('Введите m: '))
# k = int (input ('Введите k: '))

# if k % n == 0 or k % m == 0 :
#     print ('YES')
# else :
#     print ('NO')
