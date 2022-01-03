astr=input("Enter the string:")
char=input("Enter the character:")
print("Given character\n",char)
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("Number of times character present in word is:",res)
