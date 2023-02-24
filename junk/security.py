#Ask user for name, checks bool for that name. If it's not in, it will ask
#you to add it. If it is then it will ask if you would like to remove it

knownUsers = ["Tom", "Pavel", "David", "Radek", "Michal"]

while True:
    print("I'm a security system")
    user = input("What is your name?: ").strip().capitalize()
    if user in knownUsers:
        print("I know you. Your name is {}".format(user))
        remove = input("Shall I remove your from the database? (y/n): ").lower()
        if remove == "y":
            knownUsers.remove(user)
            print("You we're removed")
        else:
            print("Your we're not removed")
    else:
        add = input("I don't know you. Would you like to be added to our database? (y/n)").lower().strip()
        if add == "y":
            knownUsers.append(user)
            print("You've been added to our database {}".format(user))
        else:
            print("You haven't been added")
            
