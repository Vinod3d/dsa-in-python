sales = [1200, 450, 980, 1500, 3000]

with open('sales_data.txt', 'w') as f:
    for sale in sales:
        f.write(str(sale))
        f.write('\n')

print("File created successfully")

with open('sales_data.txt', 'r') as f:
    content = f.read()
    print(content)
    