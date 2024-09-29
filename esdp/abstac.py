class Course:
    def __init__(self,title,duration,price):
        self.title = title
        self.duration = duration
        self.price = price
        
    def enroll(self):
        print("enroll here")
        
    def getDetails(self):
        print("get details here")
        
        
class ProgrammingCourse(Course):
    def __init__(self,title,duration,price,programming_language, instructor):
        self.title = title
        self.duration = duration
        self.price = price
        self.programming_language = programming_language
        self.instructor = instructor
        
    def getDetails():
        print("get details of programming course")
        
class MathCourse (Course):
    def __init__(self,title,duration, price, level,instructor):
        self.title = title
        self.duration = duration
        self.price = price
        self.level = level
        self.instructor = instructor
        
    def getDetails():
        print("get details of math course")
        
        
class LanguageCourse(Course):
    def __init__(self,title,duration,price,language,instructor):
        self.title = title
        self.duration = duration
        self.price = price
        self.language = language
        self.instructor = instructor
        
    def getDetails():
        print("get details of language course")
        