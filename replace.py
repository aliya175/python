str1=input("Enter the string:")
char=str1[0]
str1=str1.replace(char,"$")
str1=char+str1[1:]
print("replace string is:",str1)
