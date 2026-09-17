
# 1. create a list named products containing at least 6 product names (string)
products=["laptop", "mouse", "keyboard", "phone", "tablet"]

# 2. create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product=("laptop",45000,"electronic")

# 3. print the 2nd and last product from the products list
print("2nd Product:", products[1])
print("Last Product:", products[-1])

# 4. append two new product names to products and then print the updated list.
products.append("Smart Fitness Watch")
products.append("Portable Bluetooth Speaker")

print(products)

# 5. Convert sample_product into a list , change its price and convert it back to a tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 6499.00
sample_product = tuple(sample_product_list)

print(sample_product)