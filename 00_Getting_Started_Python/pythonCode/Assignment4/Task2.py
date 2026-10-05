with open('sales_data.txt', 'r') as f:
    content = f.read()
    print(content)

# read first line
with open('sales_data.txt', 'r') as f:
    content = f.readline()
    print(content)

# read last line
with open('sales_data.txt', 'r') as f:
    lines = f.readlines()
    sales_list = [int(line.strip()) for line in lines if line.strip()]
    print(sales_list)
