
#Warmup 2: Dictionary Operations
#Create a hardcoded dictionary representing a student with these keys: name, grade, and subject

student ={
    "name": "John",
    "grade": "10",
    "subjects": ["Python", "Math", "English"]
}
#print each value 
for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print("\nUpdated dictionary:")
print(student)