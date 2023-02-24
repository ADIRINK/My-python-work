#Print a list and print parts of it
list1 = [11, 22, -4, 44, 100]
print(list1)

tom = ["A", "B", "C", 1, False]
print(tom[-2])

guga = tom[2]
print(guga)

lula = tom[:3:]
print(lula)

#Check if bool is True/False
checkIfTrue = tom[4]
if checkIfTrue == True:
    print("It's true")
if checkIfTrue == False:
    print("It's false")
    
#Take out a number from a list within a list
list2 = [1, 2, 3, [4, 5, 6], 7, 8]
print(list2[3][1])

#Print a number from a list that's in a list which itself is in a list
list3 = [1,[2,[3,0],4],5]
print(list3[1][1][0])
