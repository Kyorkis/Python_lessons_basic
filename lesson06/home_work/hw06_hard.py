# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
class Worker:
    def __init__(self, name, surname, doljnost, oklad, norma, otrabotano):
        self.name = name
        self.surname = surname
        self.doljnost = doljnost
        self.oklad = oklad
        self.norma = norma
        self.otrabotano = otrabotano

    def okl_v_chas(self):
        oklad_v_chas = self.oklad // self.norma
        return oklad_v_chas
        self.okl_v_chas = okl_v_chas

    def polychka(self):
        if self.norma < self.otrabotano:
            polychit = abs(self.otrabotano - self.norma) * (self.okl_v_chas() *2) + self.oklad
            return polychit
        
#        self.okl_v_chas = okl_v_chas

        if self.norma > self.otrabotano:
            polychit = self.oklad - (self.norma - self.otrabotano) * self.okl_v_chas() 
            return polychit
        
    
rab1 = Worker ("Петр", "Алексеев", "прораб", 22000, 140, 120 )
rab2 = Worker ("Василий", "Иванов", "плотник", 18000, 150, 180)
rab3 = Worker ("Матвей", "Бурин", "директор", 42000, 150, 160)
print ("{} {} получит: {}".format(rab1.name, rab1.surname, rab1.polychka()))
print ("{} {} получит: {}".format(rab2.name, rab2.surname, rab2.polychka()))
print ("{} {} получит: {}".format(rab3.name, rab3.surname, rab3.polychka()))


