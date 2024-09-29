form threading import *
class Mythread:
    def run(self):
        for x in range (1,11):
            print("child thread")
m=Mythread()
t=Thread(target=m.run)
t.start()
t.join()
