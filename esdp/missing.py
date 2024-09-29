n=int(input("enter size of array"))
l=[]
print("emter the numbers = ")
for i in range (n):
    c=int(input())
    l.append(c)
print("list = ",l)

s=sorted(l)
print("sorted list ", s)
print("missing number=",end=" ")
for i in range(1,s[n-1]):
    if i not in (s):
        print(i,end=" ")
    