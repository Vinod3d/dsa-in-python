## Task 1 Discount rule
def addTax(finalAmt):
    return finalAmt + finalAmt * 0.05

def discount():
    try:
        orderAmt = int(input("Enter the order amount:"))
        if(orderAmt <= 0):
            return "Invalid Input! Enter positive integers only"
        
        if orderAmt >= 2000:
            finalAmt = orderAmt - orderAmt * 0.15
            return addTax(finalAmt)
        elif orderAmt >= 1500 and orderAmt < 2000:
            finalAmt = orderAmt - orderAmt * 0.10
            return addTax(finalAmt)
        elif orderAmt >= 1000 and orderAmt < 1500:
            finalAmt = orderAmt - orderAmt * 0.07
            return addTax(finalAmt)
        else:
            return addTax(orderAmt)
    except ValueError:
        return "Invalid Input! Enter positive integers only"
   

print("Final Amount Including 5% tax is :", discount())