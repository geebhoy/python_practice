while True:
    name = input("Enter student name: ")
    if name.isalpha():
        break
    else:
        print("Enter a valid name")


age = int(input("Enter student age: "))
scores = []
while len(scores) < 3:
    try:
        score = int(input("Input the score here: "))
        if score < 0 or score > 100:
            print("Please enter a valid score between 0 and 100.")
        else:
            scores.append(score)
    except ValueError:
        print("Please enter valid numbers for scores")

skills = []
while len(skills) < 3:
        skill = str(input("Input the skill here: "))
        if not skill.isalpha():
            print("Please enter a valid skill name (letters only).")
        else:
            skills.append(skill)

print("\nStudent Information:")
print("Student Name:", name.upper())
print("Student Age:", age)
print("Student Scores:", scores)

def calculate_total(scores):
    return sum(scores)
total = calculate_total(scores)
print("Total Score:", total)

def calculate_average(scores):
    return sum(scores) / len(scores)
average = calculate_average(scores)
print("Average Score:", round(average, 2))

def calculate_grade(average):
    if average >= 70:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 45:
        return 'D'
    elif average >= 40:
        return 'E'
    else:
        return 'F'

grade = calculate_grade(average)
print("Grade:", grade)

unique_skills = set(skills)
print("Unique Skills:", unique_skills)
