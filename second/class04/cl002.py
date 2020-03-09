
from abc import abstractmethod, ABC

class AbstractPerson(ABC):
    _age = 1
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def date_of_birth(self):
        pass

class Abiturient(AbstractPerson):

    def __init__(self, name, date_of_birth, faculty):
        self._name = name
        self._date_of_birth = date_of_birth
        self._faculty = faculty

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self,value):
        self._date_of_birth = value

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self,value):
        self._faculty = value

    def age(self):
        self._age = 2020 - int(self.date_of_birth)
       #print('age is', self._age ,'years')
        return self._age

class Student(AbstractPerson):

    def __init__(self, name, date_of_birth, faculty, course):
        self._name = name
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self,value):
        self._date_of_birth = value

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self,value):
        self._faculty = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self,value):
        self._course = value

    def age(self):
        self._age = 2020 - int(self.date_of_birth)
        #print('age is', self._age ,'years')
        return self._age

class Teacher(AbstractPerson):

    def __init__(self, name, date_of_birth, faculty, position, experience):
        self._name = name
        self._date_of_birth = date_of_birth
        self._faculty = faculty
        self._position = position
        self._experience = experience

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self,value):
        self._date_of_birth = value

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self,value):
        self._faculty = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self,value):
        self._position = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self,value):
        self._experience = value

    def age(self):
        self._age = 2020 - int(self.date_of_birth)
        #print('age is', self._age ,'years')
        return self._age


#print (person.name, person.date_of_birth, person.faculty)
person1 = Abiturient('Illia', '1991', 'FEA')
person2 =  Abiturient('Dima', '1992', 'FEL')
person3 =  Abiturient('Dasha', '1995', 'IASA')
person4 = Student('Andrey', '1989', 'FIOT', '6')
person5 = Teacher('Stepan', '1987', 'FEA', 'Teacher','3')
person1.age()
person2.age()
person3.age()
person4.age()
person5.age()

myList = [person1, person2, person3, person4, person5]

for elem in (myList):
    if(isinstance(elem,Abiturient)):
        print (elem.name, elem.date_of_birth, elem.faculty, elem._age)
    elif(isinstance(elem,Student)):
        print (elem.name, elem.date_of_birth, elem.faculty, elem.course, elem._age)
    else:
        print (elem.name, elem.date_of_birth, elem.faculty,elem.position ,elem.experience, elem._age)

for elem in (myList):
    if (elem._age < 35 and elem._age > 30):
        if(isinstance(elem,Abiturient)):
            print (elem.name, elem.date_of_birth, elem.faculty, elem._age)
        elif(isinstance(elem,Student)):
            print (elem.name, elem.date_of_birth, elem.faculty, elem.course, elem._age)
        else:
            print (elem.name, elem.date_of_birth, elem.faculty,elem.position ,elem.experience, elem._age)