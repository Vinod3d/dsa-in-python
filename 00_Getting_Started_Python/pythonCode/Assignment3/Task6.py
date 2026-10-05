process_prices = [100, 500, 900, 50, 750]

def discount(p):
    p = p - (p * 0.1)
    return p

discounted_price = list(map(discount, process_prices))

filtered_discounted_price = list(
    filter(lambda x: x > 300, discounted_price)
)

print(discounted_price)
print(filtered_discounted_price)