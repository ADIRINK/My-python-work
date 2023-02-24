#This program will ask user for login and password
#Admin is one of the logins
#1234 is one of the passwords
#If correct the program will welcome user
#If incorrect program wil stop
#After loggin in the user has the ability to change the password which will log him out

login = "Admin"
password = "1234"
loggedin = False

while True:
    turnOff = input("Do you wish to login?(y/n): ")
    if turnOff == "n":
        break
    if turnOff == "y":
        while loggedin == False:
            print("To enter you must enter the login and password")
            pLogin = input("Login: ")
            if pLogin == login:
                 print("Login is correct")
                 pPassword = input("Password: ")
                 if pPassword == password:
                     print("Password is correct")
                     loggedin = True
                 if pPassword != password:
                    print("Password ERROR")
            if pLogin != login:
                print("Login ERROR")

        while loggedin == True:
            print("You are now logged in")
            chngPass = input("Would you like to change your password?(y/n): ").strip()
            if chngPass == "n":
                logOut = input("Type 'Exit' to logout: ")
                if logOut == "Exit":
                    loggedin = False
            if chngPass == "y":
                newPass = input("Input new password: ")
                password = newPass
                print("New password set")
                loggedin = False
        
    
