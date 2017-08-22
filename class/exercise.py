class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def fullpay(self):
        return '{}'.format(self.pay)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        print self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def set_num_of_employees(cls, number):
        cls.num_of_emps = number

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    @staticmethod
    def is_effective(name):
        print "%s is effective." % name

class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

dev_2 = Developer('Eric','Babjac', 140000, 'Python')

print(dev_2.email)
print(dev_2.prog_lang)

print Developer.raise_amount
print "The number of Developer employees is", Developer.num_of_emps

import datetime
mydate = datetime.date(1997, 03, 12)

Employee.is_effective('Jerry')

print(Employee.is_workday(mydate))

emp_1 = Employee('Bailey', 'Hosea', 50000)
emp_2 = Employee('John', 'Hampster', 60000)

emp_string_1 = 'John-Doe-70000'
emp_string_2 = 'Steve-Smith-60000'
emp_string_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_string_1)
new_emp_2 = Employee.from_string(emp_string_2)
new_emp_3 = Employee.from_string(emp_string_3)

breaker = '-' * 10

print new_emp_1.fullname()
print new_emp_1.email
print new_emp_1.fullpay()
print breaker
print new_emp_2.fullname()
print new_emp_2.email
print new_emp_2.fullpay()
print breaker
print new_emp_3.fullname()
print new_emp_3.email
print new_emp_3.fullpay()

Employee.set_num_of_employees(55)
Employee.set_raise_amount(1.07)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.num_of_emps)
