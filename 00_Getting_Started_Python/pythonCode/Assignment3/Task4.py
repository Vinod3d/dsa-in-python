gst = lambda price:price + (0.18 * price)
prices = [100, 250, 400, 1200, 50]

prices_with_gst = map(gst, prices)


print(list(prices_with_gst))
print(list(prices))