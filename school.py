class Person :
    def __init__(self,name,age,id):
        self.__name=name
        self.__age=age
        self.__id=id

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age>0:
            self.__age=new_age
        else:
            print("Age isnt nagative!")

    def set_id(self,new_id):
        self.__id=new_id

    def set_name(self,newname):
        if isinstance(newname,str):
           self.__name=newname

        else:
            print("Name is Latter")

       
    
class Student(Person):
    def __init__(self, name, age, id,marks,grade):
        super().__init__(name, age, id)
        self.__marks=marks
        self.__grade=grade 

    def get_marks(self):
        return self.__marks
    def get_grade(self):
        return self.__grade
    def set_mark(self,new_mark):
       
        if isinstance(new_mark,int) and 0<=new_mark<=100:
              self.__marks=new_mark 
             

        else:
            print("mark is <100 & int")


    def show (self):
        
        print(f"Student name ={self.get_name()} age ={self.get_age()} id ={self.get_id()} mark ={self.get_marks()} grade ={self.get_grade()}")

class Teacher(Person):
    def __init__(self, name, age, id,sub,salary):
        super().__init__(name, age, id)

        self.sub=sub
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    def set_salary(self,newsalary):
        if newsalary>3000:
            self.__salary=newsalary
        else :
            print("The lowest salary is 3000 tkka")
    def show(self):
        print(f"Teacher name ={self.get_name()} age ={self.get_age()} sub ={self.sub} Salary ={self.get_salary()}")
    
    
st1=Student("arafat",23,243,80,"A+")
st1.set_id(244)
st1.set_mark(90)
#st1.set_name(12)
st1.show()

t1=Teacher("maimun",34,443,'csi11',323442)
t1.set_salary(2300)
t1.set_age(30)
t1.show()