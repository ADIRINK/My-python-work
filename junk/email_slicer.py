#Get user email adress
email = input("What is your email adress?: ").strip()

#Slice out username
user = email[:email.index("@")]

#Slice out domain name
domain = email[email.index("@")+1:]

#Format message
output = "Your username is {} and your domain is {}".format(user, domain)

#Display output message
print(output)
