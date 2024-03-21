class Student:
    def fun(self,rollno,per):
        self.rollno=rollno
        self.per=per
    def display_data(self):
        print(self.rollno,self.per)

s1 = Student(123,69.9)
s1.display_data( )
