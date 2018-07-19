# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Student:
    def __init__ (self,firstname,lastname,surname,dad,mom,class_room,class1,class2,class3):
        self.firstname = firstname
        self.lastname = lastname
        self.surname = surname
        self.dad = dad
        self.mom = mom
        self.class_room = class_room
        self.class1 = class1
        self.class2 = class2
        self.class3 = class3
        self.fullname = ("{} {} {}".format (self.firstname, self.lastname, self.surname))            
    def get_name(self):
        return ("{}  {}  {}".format(self.firstname , self.lastname , self.surname))
    
    def get_parents(self):
        return ("Родители ученика- {} Мать - {}, отец - {}".format(self.fullname,self.mom, self.dad))

vasya = Student ("Пануков", "Василий", "Викторович", "Пануков Виктор Владимирович", "Панукова Ирина Дмитриевна", "5 A", "phisik", "mathematic", "literal")
kolya = Student ("Ижорский", "Николай", "Петрович", "Ижорский Петр Васильевич", "Ижорская Анна Валерьевна", "5 A", "phisik", "mathematic", "literal")
for students in Student:
    print (students.class_room)
#print(vasya.get_name())
print (vasya.get_parents())
print (kolya.get_parents())