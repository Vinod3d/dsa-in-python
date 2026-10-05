daily_sale = [200, 150, 0, 400, 50, -1, 300]
total_sale = 0
for sale in daily_sale:
    if sale < 0:
        break
    elif sale == 0:
        continue
    else:
        total_sale += sale
print("Total sale is :", total_sale)