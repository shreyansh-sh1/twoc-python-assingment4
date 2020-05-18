a=[]
n=int(input("Enter number of elements of tuple: "))
print("Enter elements of tuple: ")
for i in range(n):
    b=input()
    a.append(b)
tuple(a)
c=input("Enter element whose occurrence you want to know: ")
print(c,"occurs",c.count(c),"times")

# Code by shreyansh sharma