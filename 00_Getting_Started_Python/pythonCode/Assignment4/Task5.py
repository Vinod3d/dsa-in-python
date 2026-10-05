# Task 5: Create Product Info File

filename = "products.txt"

with open(filename, "w") as file:
    for i in range(1, 4):
        print(f"Enter details for Product {i}:")
        name = input("Product Name: ").strip()
        price = input("Price: ").strip()
        
        file.write(f"{name} | {price}\n")

with open(filename, "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            parts = clean_line.split(" | ")
            product_name = parts[0]
            price = parts[1]
            print(f"Product: {product_name:<15} | Price: ₹{price}")