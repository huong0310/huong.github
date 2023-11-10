day=int(input("Day: "))
month=input("Month: ")
if month=="January" and day==1:
    print("Holiday: New year’s day")
elif month=="July" and day==1:
    print("Holiday: Canada day")
elif month=="December" and day==25:
    print("Holiday: Christmas day")
else:
    print("Not correspond")