with open('sales_data.txt', 'a') as f:
    f.write("5000\n")
    f.write("2500\n")
    f.write("1700\n")

# verify
with open('sales_data.txt', 'r') as f:
    content = f.read()
    print(content)