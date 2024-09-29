class Time:
    def __init__(self):
        print("contructor is cslled ")
    def __del__(self):
        print(" descontructor is called")
t=Time()
t=None
print("applicatin is ended")