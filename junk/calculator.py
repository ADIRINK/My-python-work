def combineNum(no1, no2):
    number = int(no1) + int(no2)
    return number

def subtractNum(no1, no2):
    number = int(no1) - int(no2)
    return number

def divideNum(no1, no2):
    number = int(no1) / int(no2)
    return number

def multiplyNum(no1, no2):
    number = int(no1) * int(no2)
    return number

def enterNumbers():
    no1 = input("Enter Number: ").strip()
    no2 = input("Enter another Number: ").strip()
    return no1, no2

def menu():
    print("What do you want to do?")
    print("1. X + Y =")
    print("2. X - Y =")
    print("3. X / Y =")
    print("4. X * Y =")
    print("5. Quit")
    textResult = "Result is:"
    menuSel = input("Select: ")

    if menuSel == "1":
        no1, no2 = enterNumbers()
        calResult = combineNum(no1, no2)
        print(textResult, calResult)
    if menuSel == "2":
        no1, no2 = enterNumbers()
        calResult = subtractNum(no1, no2)
        print(textResult, calResult)
    if menuSel == "3":
        no1, no2 = enterNumbers()
        if ZeroDivisionError:
            print("Error. Can't divide by zero")
            return
        calResult = divideNum(no1, no2)
        print(textResult, calResult)
    if menuSel == "4":
        no1, no2 = enterNumbers()
        calResult = multiplyNum(no1, no2)
        print(textResult, calResult)
    if menuSel == "5":
        quit()
    else:
        print("Error")
        return

while True:
    menu()