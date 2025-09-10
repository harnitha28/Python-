a=[]
n=int(input("enter elements in the list"))
for i in range (0,n):
    m=int(input("enter the elemts"))
    a.append(m)
print(a)
print(a[0])
print(a[-1])
print(a[3])
print(a[1:])
print(a[-5:])
print(a[1:7])
print(a[-7:-0])
a.extend([3,5,8])
print(a)
a.insert(4,56)
print(a)

