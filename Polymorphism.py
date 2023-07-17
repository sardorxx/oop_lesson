

class Father:
    def __init__(self, name, lastname, gender, profession, hobby, char):
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.profession = profession
        self.hobby = hobby
        self.char = char

    def get_name(self):
        return self.name

    def set_name(self, a):
        self.name = a

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, b):
        self.lastname = b

    def get_gender(self):
        return self.gender

    def set_gender(self, c):
        self.name = c

    def get_profession(self):
        return self.profession

    def set_profession(self, d):
        self.profession = d

    def get_hobby(self):
        return self.hobby

    def set_hobby(self, e):
        self.hobby = e

    def get_char(self):
        return self.char

    def set_char(self, f):
        self.char = f

    profession_ = property(fget=None, fset=None, fdel=None)


class Mother(Father):

    def __init__(self, name, lastname, gender, profession, hobby, char, age):
        super().__init__(name, lastname, gender, profession, hobby, char)
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, f):
        self.age = f


class Child(Mother):
    def __init__(self, name, lastname, gender, profession, hobby, char, age, university, grade):
        super().__init__(name, lastname, gender, profession, hobby, char, age)
        self.university = university
        self.grade = grade

    def get_university(self):
        return self.university

    def get_grade(self):
        return self.grade

    def set_university(self, h):
        self.university = h

    def set_grade(self, m):
        self.grade = m


father = Father('John', 'Tom', 'Male', 'Banker', 'Reading books', 'Kind')
mother = Mother('Suzan', 'Flea', 'Female', 'Assistance', 'Cooking', 'Funny', 23)
child = Child('Suzan', 'Flea', 'Female', 'Assistance', 'Cooking', 'Funny', 23, 'INHA', 5)
setattr(father, 'name', 'Envy')
setattr(father, 'lastname', 'Brown')
setattr(father, 'gender', 'Male')
setattr(father, 'profession', 'Trader')
setattr(father, 'hobby', 'Shopping')
setattr(father, 'char', 'Talk more')

setattr(mother, 'name', 'Anna')
setattr(mother, 'lastname', 'Buffer')
setattr(mother, 'gender', 'Female')
setattr(mother, 'profession', 'House wife')
setattr(mother, 'hobby', 'Chatting')
setattr(mother, 'char', 'Friendly')
setattr(mother, 'age', 29)

setattr(child, 'name', 'Gray')
setattr(child, 'lastname', 'Buffer')
setattr(child, 'gender', 'Male')
setattr(child, 'profession', 'Student')
setattr(child, 'hobby', 'Drawing')
setattr(child, 'char', 'Always happy')
setattr(child, 'age', 11)
setattr(child, 'university', 'MDIS')
setattr(child, 'grade', 4)


print("""         Father  """)
print('Harakter     :', father.get_char())
print('Hobbiy       :', father.get_hobby())
print('Jinsi        :', father.get_gender())
print('Kasbi        :', father.get_profession())
print('Familiya     :', father.get_lastname())
print('Ism          :', father.get_name())

print("""         Mother  """)
print('Harakter     :', mother.get_char())
print('Hobbiy       :', mother.get_hobby())
print('Jinsi        :', mother.get_gender())
print('Kasbi        :', mother.get_profession())
print('Familiya     :', mother.get_lastname())
print('Ism          :', mother.get_name())
print('Yoshi        :', mother.get_age())

print("""         Child  """)
print('Harakter     :', child.get_char())
print('Hobbiy       :', child.get_hobby())
print('Jinsi        :', child.get_gender())
print('Kasbi        :', child.get_profession())
print('Familiya     :', child.get_lastname())
print('Ism          :', child.get_name())
print('Yoshi        :', child.get_age())
print('Universitet  :', child.get_university())
print('Baho         :', child.get_grade())
