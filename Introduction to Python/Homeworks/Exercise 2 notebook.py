#read all the content of the file in one variable 
file=open("student_names.txt")
students=file.readlines() 

# read n first lines 
n=3
print("the n first elements are :",students[0:n])

#read n last line 
n=3
nb_elem=len(students)
print("the n last elements are :",students[nb_elem-n:nb_elem])

# if the x name is in the file 
x="khedir meriem\n"
print("the name x is in my file :", x in students)

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.



import string
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
