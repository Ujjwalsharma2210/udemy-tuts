class Emplyoee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def name(self):
        return "{} {}".format(self.first, self.last)


emp1 = Emplyoee("One", "Sur", 50000)
emp2 = Emplyoee("Two", "Sur", 40000)
emp3 = Emplyoee("Three", "Sur", 70000)
