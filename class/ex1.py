class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def everything(self):
        return '{} \n{} \n{} \n{}'.format(self.first,
        self.last, self.pay, self.email)

    def trial(self):
        return '%s' % self.first


emp_1 = Employee('Bailey', 'Hosea', 90000)
emp_2 = Employee('Devon', 'Babjac', 90000)

print (emp_1.fullname())
print (emp_2.fullname())

print emp_1.everything()
print emp_2.everything()

print emp_1.trial()
