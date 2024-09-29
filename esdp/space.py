class space:
    def __init__(self,input1,input2):
        self.input1=input1
        self.input2=input2
    def remove_character(self,input1,input2):
        result = self.input1.replace(self.input2, '')

input1 = input("Enter a 1 String: ")
input2 = input("Single character want to remove: ")
s=space(input1,input2)
s.remove_character(input1,input2)
