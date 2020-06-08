def sortStudents(students):
    students.sort(key=lambda full_name: full_name.split()[-1])
    return students

students = ["John Smith", "Jacky Mon Simonoff", "Lucy Smith", "Angela Zimonova"]
print(sortStudents(students))