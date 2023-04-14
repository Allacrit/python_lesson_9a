"""
Реализовать дескрипторы для любых двух классов.
"""


class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class NonNumbers:
    def __set__(self, instance, value):
        if isinstance(value, int):
            raise ValueError("Имя/фамилия не может быть числом")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:
    wage = NonNegative()
    bonus = NonNegative()
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
    def __str__(self):
        return str(f'Заработная плата: {self.wage}\n'
                   f'Премия: {self.bonus}\n')


class Position(Worker):
    name = NonNumbers()
    surname = NonNumbers()
    def get_full_name(self):
        print(f"Имя: {self.name}")
        print(f"фамилия: {self.surname}")

obj = Position("Вася", "Петров", "слесарь", 50000, 10000)
obj.get_full_name()
print(obj)

obj.name, obj.surname = "Иван", "Иванов"
obj.get_full_name()
obj.wage, obj.bonus = 60000, 15000
print(obj)