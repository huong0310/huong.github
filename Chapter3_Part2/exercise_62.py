price=[4.95,9.95,14.95,19.95,24.95]
print ("The Original Price | The Discount Amount | The New Price")
for i in price:  
    TheDiscountAmount=round(i*0.6,2)
    TheNewPrice=round(i-TheDiscountAmount,2)
    print("    ",i,"               ",TheDiscountAmount,"             ", TheNewPrice)
