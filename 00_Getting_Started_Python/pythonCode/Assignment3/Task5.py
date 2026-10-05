prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive = lambda p: p > 500
cheap = lambda p: p <= 500

expensive_prices = list(filter(expensive, prices))
print("expensive prices are ", expensive_prices)
cheap_prices = list(filter(cheap, prices))
print("cheap prices are ", cheap_prices)
print("Original prices", prices)