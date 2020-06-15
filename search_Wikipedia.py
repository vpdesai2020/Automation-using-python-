import wikipedia

def search(self):
	print(wikipedia.summary(self))
	

input_qry=input("what you want to search : ")
search(input_qry)
