import datetime
date=datetime.date.today()
currentyear=int(date.strftime("%Y"))
print("Enter the last year")
endyear=int(input())
print("List of Leap Years:")
for year in range(currentyear,endyear):
    if((year%4==0)and(year%100!=0)or(year%400==0)):
        print(year)
