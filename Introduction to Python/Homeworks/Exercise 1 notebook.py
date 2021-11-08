#Our list Ls 

Ls=[]

#Initialisation of our list with elements from 1 to 299

for i in range(1,300):
    Ls.append(i)

#The legth of our list 

print("The length of our list is =",len(Ls))

#All the squared values

for i in Ls:
    print("the squared value of :",i," is :" ,i**2)

# Is 57 in the list

print(" 57 is in the list :", 57 in Ls)