## Task 2

orderAmt = [1200, 2500, 800, 1750, 3000]

## Task 1 Discount rule
def addTax(finalAmt):
    return finalAmt + finalAmt * 0.05

def discount(amt):
    try:
        if(amt <= 0):
            return "Invalid Input! Enter positive integers only"
        
        if amt >= 2000:
            finalAmt = amt - amt * 0.15
            return "15%", addTax(finalAmt)
        elif amt >= 1500 and amt < 2000:
            finalAmt = amt - amt * 0.10
            return "10%", addTax(finalAmt)
        elif amt >= 1000 and amt < 1500:
            finalAmt = amt - amt * 0.07
            return "7%", addTax(finalAmt)
        else:
            return "No discount", addTax(amt)
    except ValueError:
        return "Invalid Input! Enter positive integers only"

totalRevenue = 0
discountNum = 0

print("|--------------|-----------|---------------|"  )
print("| Order amount | Discount  | Final amount  | ")
print("|--------------|-----------|---------------|"  )
for amount in orderAmt:
    discountPercent, finalAmount = discount(amount)
    if discountPercent != "No discount":
        discountNum += 1
    totalRevenue += finalAmount
    print(f"|    {amount}     |   {discountPercent}    | {finalAmount:.2f}    |")
print("|---------------|-----------|---------------|"  )
print("Total Revenue is :", totalRevenue)
print("Total number of orders with discount is :", discountNum)