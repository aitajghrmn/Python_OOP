student = {
    "name": "Ali",
    "age": 20,
    "grade": 85
}

print(student["name"])
student["grade"]=90
student["city"]="Baku"


for key in student:
    print(key, student[key])