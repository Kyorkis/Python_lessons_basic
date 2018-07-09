# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#def my_round(number, ndigits):
#    pass
   

#print(my_round(2.1234567, 5))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))
#def my_round(number, ndigits):
#    number = number * (10 ** ndigits)
#    if float(number) - int(number) > 0.5:
#         number = number // 1 + 1
#    else:
#         number = number // 1
#    return number / (10 ** ndigits)
#print(my_round(2.1234567, 1))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#def lucky_ticket(ticket_number):
#    pass


#print(lucky_ticket(123006))
#print(lucky_ticket(12321))
#print(lucky_ticket(436751))
#def lucky_ticket(ticket_number):
#    lucky_ticket = lambda x :(lambda x : 'yes' if sum(x[:3]) == sum(x[3:]) else 'no')(map(int, list(str(x)))) 
#    print(lucky_ticket(129567))


#def lucky_ticket(ticket_number):
 #   for i in range (ticket_number):
 #       if sum(i[:3])== sum(i[3:]):
#               print ("Lucky!!")
#        else:
#            print ("Bad")
 #           return(x)
#ticket_number = int(input())
#print (x)



#def lucky_ticket(ticket_number):
 #   if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
#        return 'Некорректный номер билета'
#    else:
#        ticket_number1 = list(str(ticket_number))
#        for ticket in ticket_number1:
#        if ticket[0] + ticket[1] + ticket[2] == ticket[3] + ticket[4] + ticket[5]:
#            return 'Билет %s счастливый' %ticket_number
#        else:
#            return 'Билет %s несчастливый' %ticket_number

#number = int(input('Введите номер билета:'))
#number = 123456
#print(lucky_ticket(number))
def lucky_ticket(ticket_number):
    lucky_ticket = lambda x : (lambda x : "YES" if sum(x[:3]) == sum [3:] else "NO")(list(map(int,list(str(x)))))
ticket_number = 123456
print(lucky_ticket)

#FUNCTION = lambda x : (lambda x : 'yes' if sum(x[:3]) == sum(x[3:]) else 'no')(list(map(int, list(str(x)))))

#INPUT=654456
#RESULT = FUNCTION(INPUT)
#print(RESULT)
