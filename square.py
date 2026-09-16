def calc(num1, num2, opr):
    try:
        if opr == "+":
            return num1 + num2
        elif opr == "-":
            return num1 -  num2
        elif opr == "*":
            return num1 *  num2
        elif opr == "/":
            return num1 /  num2
        elif opr == "%":
            return num1 %  num2
        else:
            return "Pls enter a correct operator"
    except ZeroDivisionError:
        return "Pls input a non-zero number for division"
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    opr = input("Enter operator: ")

    a = calc(num1, num2, opr)
    print(a)
except ValueError:
    print("error")