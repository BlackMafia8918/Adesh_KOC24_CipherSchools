"""
continue statement -
- it's also used in loops

"""

#for i in range(1,11):
#    if i == 6:
#        print(i, "Hello")
#        continue
    #    print(i, "Hye")
    #   print("Out of the loop")

for i in range(1,101):
    if i%7==0:
        continue
    elif i%2==0 and i%3==0 and i%5==0:
        break
    print(i)


#print ("starting of loop")
#for i in range(1, 11):
#    if i == 6:
#        print(i,"hello")
#        continue
#    print(i,"hye")
#    continue 
#    print("out of loop")
