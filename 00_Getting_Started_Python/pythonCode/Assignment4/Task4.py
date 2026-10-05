with open('sales_data.txt', 'r') as f:
    lines = f.readlines()
    sales_list = [int(line.strip()) for line in lines if line.strip()]
    print(sales_list)
    total_sales = sum(sales_list)
    highest_sales = max(sales_list)
    lowest_sales = min(sales_list)
    average_sales = total_sales / len(sales_list)
    print("Total Sales: ", total_sales)
    print("Highest Sales: ", highest_sales)
    print("Lowest Sales: ", lowest_sales)
    print("Average Sales: ", average_sales)