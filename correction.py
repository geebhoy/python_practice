name = input("Enter student name: ")
scores = []

while len(scores) < 3:
    try:
        score = int(input("Enter a score: "))
        scores.append(score)
    except ValueError:
        print("Please enter a valid number")