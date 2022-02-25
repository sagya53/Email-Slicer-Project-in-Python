email = input("Enter Your email id : ")
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("After slicing the email id :")
print("UserName : ",username)
print("Domain : ",domain)
