class Team:
     

     def info_get(self):
        self.c_n=input("enter country name = ")
        self.n_p=input("enter player name = ")
        self.age=int(input("enter age of player = "))
        self.n_m=int(input("enter no of matches played="))
        self.bat_a=float(input("enter batting average ="))
        self.ball_a=float(input("enter balling average ="))
   

     def showinfo(self):
        print(self.c_n, end="       ")
        print(self.n_p, end="      ")
        print(self.age, end="       ")
        print(self.n_m, end="      ")
        print(self.bat_a, end="     ")
        print(self.ball_a)



t=Team()
t1=Team()
t2=Team()
t3=Team()
t4=Team()

t.info_get()
t1.info_get()
t2.info_get()
t3.info_get()
t4.info_get()
print("country name   player name   no of matches   batting avg     balling avg")
t.showinfo()
t1.showinfo()
t2.showinfo()
t3.showinfo()
t4.showinfo()