#if, else, else if
num1 = 100
num2 = 101

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("ERROR")

#not, and, or
c = 1
d = 2
msg = "c = {}, d = {}".format(c,d)
print(msg)

if (c > d and d > 1):
    print(" 'True and True' ")

if not (c > d and d > 1):
    print(" 'False and True' ")

if (c > d or d > 1):
    print(" 'or condition' ") 

if not ((c > 3 and d > 3) or (c < d and d > 3)):
    print(" 'if not or' ")
