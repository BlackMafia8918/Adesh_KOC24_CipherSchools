"""# import keyword library
import keyword
keyword_list = keyword.kwlist
print("No. of keywords present in current version :" len(keyword_list))
   
print(keyword_list)
"""




#Instead of writing this massive Python code
#we can also code this in a different way

#Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword
# initializing strings for testing while putting them in an array
keys = ["lambda", "gamma", "class"]

for i in range(len(keys)):
	if keyword.iskeyword(keys[i]):
		print(keys[i]  + ": True")
	else:
		print(keys[i]  + ": False")