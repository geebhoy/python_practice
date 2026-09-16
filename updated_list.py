students = {
    "Gideon": {
        "age": 21,
        "skills": ["Python", "HTML", "CSS"],
        "scores": [85, 90, 78]
    },
    "Alex": {
        "age": 22,
        "skills": ["Python", "JavaScript"],
        "scores": [92, 88, 95]
    }
}

gideon_age = students["Gideon"]["age"]
gideon_skill = students["Gideon"]["skills"][1]
students["Gideon"]["scores"][2] = 85
append_skill = students["Gideon"]["skills"].append("JavaScript")
total_scores = sum(students["Gideon"]["scores"])
gideon_skills = set(students["Gideon"]["skills"])
gideon_skills.add("go")
print("Gideon's age:", gideon_age)
print("Gideon's second skill:", gideon_skill)
print("Gideon's skills:", gideon_skills)
for Gideon, details in students.items():
    print(f"{Gideon}: {details}")
    print(f"Age: {details['age']}")
    print(f"Skills: {details['skills']}")
    print(f"Scores: {details['scores']}")