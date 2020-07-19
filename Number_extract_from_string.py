import re
your_string = input("Enter string: ")

temp=re.findall(r'\d+',your_string)
res=list(map(int,temp))

print("Numbers are : " + str(res))