import re
mail_format='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(self):
    if (re.search(mail_format,self)):
        print("Entered E-mail: "+self+" ,is valid")
    else:
        print("Entered E-mail"+self+" ,is NOT valid")

if __name__== '__main__' :
    email=input("Enter E-mail address: ")
    check(email)
