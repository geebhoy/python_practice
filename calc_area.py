def calculate_area(length, width):
    return length * width

calculate_area(10, 5)

try:
    num = int(input("Enter a number: "))
except:
    print("Please enter a valid number.")