prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}

discount_percent = float(input("Enter discount percentage (%): "))

report_filename = "discount_report.txt"

with open(report_filename, 'w') as file:
    file.write("Product | Original Price | Discounted Price\n")
    for product, orig_price in prices.items():
        discount_amount = (orig_price * discount_percent) / 100
        discounted_price = orig_price - discount_amount
        
        file.write(f"{product:^15} | {orig_price:^10} | {discounted_price:^10.2f}\n")

with open(report_filename, 'r') as file:
    print(file.read())