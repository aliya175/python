list=['aravind','aparna']
print("The origial list \n"+str(list))
res=[ord(ele)for sub in list for ele in sub]
print("The ASCII list is:\n"+str(res))
