from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self,title,duration,price):
        self.title = title
        self.duration = duration
        self.price = price
    
    def enroll(self):
        return "You are enrolled."
    @abstractmethod
    def get_details(self):
        pass
class ProgrammingCourse(Course):
    def __init__(self,title,duration,price, pro_lan, instr):
        super().__init__(title,duration,price)
        self.pro_lan = pro_lan
        self.instr = instr

def get_details(self):
        print("Title: ", self.title) 
        print("Duration: ", self.duration)
        print("Price: ", self.price)
        print("Programming Language: ", self.pro_lan)
        print("Instructor: ", self.instr)  

a = ProgrammingCourse("Start with Python", 3, 3000, "Python", "ali")    
print(a.get_details())    
    
print(a.enroll())