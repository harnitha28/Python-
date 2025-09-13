m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))
total = m1 + m2+ m3 + m4 + m5
print("total",total)
avg = total / 5
if m1>40 and m2>40 and m3>40 and m4>40 and m5>40:
    print("Result is pass")
else :
    print("Result is fail:")
if avg >= 90:
    print("grade = A")
elif avg >= 75:
    print("grade = B") 
elif avg >= 60:
    print("grade = C")
elif avg >= 40:
   print(" grade = D ")
else:
    print("grade F (Fail)")
