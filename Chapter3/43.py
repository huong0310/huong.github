banknote=int(input("Amount= "))
if banknote==1:
    Individual="George Washington"
elif banknote==2:
    Individual="Thomas Jefferson"
elif banknote==5:
    Individual="Abraham Lincoln"
elif banknote==10:
    Individual="Alexander Hamilton"
elif banknote==20:
    Individual="Andrew Jackson"
elif banknote==50:
    Individual="Ulysses S. Grant"
elif banknote==100:
    Individual="Benjamin Franklin"
    
else:
    Individual="Not exist"
print(Individual)