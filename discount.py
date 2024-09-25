purchase_amount = input("Enter your purchase amount")
purchase_amount = float(purchase_amount)
discount = 0
final_price = 0
final_price = purchase_amount - discount
final_price = int(final_price)
if purchase_amount >= 1000:
    discount = 0.1 * purchase_amount

elif purchase_amount >= 500 and purchase_amount < 1000:
    discount = 0.05 * purchase_amount
else:
    discount = 0
final_price = purchase_amount - discount
print("The final price after discount is = $", final_price)  
    

    