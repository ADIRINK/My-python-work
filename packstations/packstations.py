ps1 = ["122", "435", "902", "102"]
ps2 = []
ps3 = ["443", "202"]
ps4 = ["663"]
qP = False
validSlct = {"ps1", "1", "ps2", "2", "ps3", "3", "ps4", "4"}

#Select Packstation(PS) and either check what numbers there are, add new numbers or delete old numbers

while True:
    while qP == False:
        print("1. Write new number")
        print("2. Delete old number")
        print("3. Check written numbers")
        print("4. Exit program")
        psSelect = input("Choose option: ").strip()
        
        if psSelect == "1":
            print("On which table you want to write?")
            print("PS1, PS2, PS3, PS4")
            psSlct = input().lower()
            if psSlct not in validSlct:
                print("Error. Wrong option")
                break
            else:
                try:
                    psNumber = int(input("What number do you wish to input?: "))
                    psNumber = str(psNumber)
                except ValueError:
                    print("Error. Not a number")
                    break
                else:    
                    if psSlct == "ps1" or psSlct == "1":
                        ps1.append(psNumber)
                        psList = ps1
                    if psSlct == "ps2" or psSlct == "2":
                        ps2.append(psNumber)
                        psList = ps2
                    if psSlct == "ps3" or psSlct == "3":
                        ps3.append(psNumber)
                        psList = ps3
                    if psSlct == "ps4" or psSlct == "4":
                        ps4.append(psNumber)
                        psList = ps4
                    print(psNumber, "has been added to PS")
                    print(psList)
                    break
                
        if psSelect == "2":
            print("From which table you want to delete?")
            print("PS1, PS2, PS3, PS4")
            psSlct = input().lower()
            if psSlct not in validSlct:
                print("Error. Wrong option")
                break
            else:
                if psSlct == "ps1" or psSlct == "1":
                    print(ps1)
                    psList = ps1
                if psSlct == "ps2" or psSlct == "2":
                    print(ps2)
                    psList = ps2
                if psSlct == "ps3" or psSlct == "3":
                    print(ps3)
                    psList = ps3
                if psSlct == "ps4" or psSlct == "4":
                    print(ps4)
                    psList = ps4
                try:
                    psNumber = int(input("What number do you wish to delete?: "))
                    psNumber = str(psNumber)
                except ValueError:
                    print("Error. Not a number")
                    
                if psNumber not in psList:
                    print("Error. Number not in list")
                    
                if psNumber in psList:
                    psList.remove(psNumber)
                    print(psNumber,"has been deleted")
                    print(psList)
                    break
                
        if psSelect == "3":
            print("PS1", ps1)
            print("PS2", ps2)
            print("PS3", ps3)
            print("PS4", ps4)

        if psSelect == "4":
            qP = True
            break

        if psSelect != "1" or "2" or "3" or "4":
                print("Error. Wrong option")

    if qP == True:
        print("Closing..")
        break
        
