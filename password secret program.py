#Harry Robinson
#10-10-2014
#Password secret program

password = ""
while password != "secret":
    password = input("Give the password: ")
    if password == "secret":
        print("Thanks you entered the right password")
    else:
        print("Incorrect password try again")
        
