student = {
    "name": "Gideon",
    "age": 20,
    "course": "Computer Science",
    "scores": [75, 88, 92],
}
student["age"] = 21
student["skills"] = ["Python", "HTML", "CSS"]
student["grade"] = "A"
student["scores"][2] = 95

print("Student course: ", student["course"])
print("Student third score: ", student["scores"][2])
print(student.get("email") or "NO email avab")
for key, value in student.items():
    print(f"{key}: {value}")