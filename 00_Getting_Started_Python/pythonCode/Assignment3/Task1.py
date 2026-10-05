def apply_discount(price, discount_percent=5 ):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price



print(f"Price after discount of 10% on 700 is {apply_discount(700,10)}")
print(f"default discount of 5% on 500 is {apply_discount(500)}")
print(f"test function {apply_discount(1000, 10)}")

        
    