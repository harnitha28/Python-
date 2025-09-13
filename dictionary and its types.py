student_marks = {"hari": 85,"aneek": 92,"pavi": 78,"anu": 95}
print("Student Marks:", student_marks)
print("Marks of hari:", student_marks["hari"])
student_marks["ram"] = 88
print( student_marks)
student_marks["aneek"] = 89
print( student_marks)
student_marks.pop("pavi")
print( student_marks)
print("Students and Marks:")
for name, marks in student_marks.items():
    print(name, ":", marks)
