"""
1 - exercise
"""
from _datetime import datetime


class Circle:
    """
    This program is calculate the area and length of circle
    """
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def take_the_area(self):
        """

        : return: area
        """
        area = 2 * self.pi * self.radius
        return area

    def take_the_length(self):
        """

        : return: length
        """
        length = self.pi * self.radius ** 2
        return length

    def __repr__(self):
        return f'{self.pi}{self.radius}'


case = Circle(3)
print(case.take_the_area(), case.take_the_length())


class Person:
    """
    This program returns person age
    """
    def __init__(self, name, country, birth_year: datetime):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def return_person_age(self):
        """
        : returns: Person age
        """
        return

    def __repr__(self):
        return f'{self.name}{self.country}{self.birth_year}'

birth_years = datetime(2005, 2, 8, 5, 30, 24)
year = Person('John ', ' Uzbekistan ', birth_years)
print(year)


class Circle:
    """
    This program is calculate the area and length of circle
    """
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def take_the_area(self):
        """

        : return: area
        """
        area = 2 * self.pi * self.radius
        return area

    def take_the_length(self):
        """

        : return: length
        """
        length = self.pi * self.radius ** 2
        return length

    def __repr__(self):
        return f'{self.pi}{self.radius}'


case = Circle(9)
print(case.take_the_area(), case.take_the_length())


class Triangle:
    """
    This program is calculate the area and length of triangle
    """
    def __init__(self, ab, ba, cb):
        self.ab = ab
        self.ba = ba
        self.cb = cb

    def take_the_area(self):
        """

        : return: area
        """
        area = self.ab * self.ba / 2
        return area

    def take_the_length(self):
        """

        : return: length
        """
        length = self.ab + self.ba + self.cb
        return length

    def __repr__(self):
        return f'{self.ab}{self.ba}{self.cb}'


case = Triangle(3, 9, 8)
print(case.take_the_area(), case.take_the_length())


b = input('   ')
a = input(' ')
c = input('   ')


class Calculator:
    """
    Calculator
    """

    def __init__(self, sign, num1, num2):
        self.sign = sign
        self.num1 = num1
        self.num2 = num2

    def calculate_num(self):
        """

        : return: Answer
        """
        if self.sign == '+':
            g = int(self.num1)
            p = int(self.num2)
            m = g + p
            return m
        elif self.sign == '-':
            g = int(self.num1)
            p = int(self.num2)
            m = g - p
            return m
        elif self.sign == '*':
            g = int(self.num1)
            p = int(self.num2)
            m = g * p
            return m
        elif self.sign == '/':
            g = int(self.num1)
            p = int(self.num2)
            m = g / p
            return m
        else:
            return 'Error'

    def __repr__(self):
        return f'{self.sign}{self.num1}{self.num2}'

hello = Calculator(a, b, c)
print(hello.calculate_num())
