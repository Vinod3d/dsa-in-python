prices = [120, 350, "abc", 500, -200, 800]
total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price
        print(f"Added {price}. Running total: {total}")

    except TypeError as e:
        print(f"Skipping invalid item '{price}': {e}")

    except ValueError as e:
        print(f"Skipping invalid item '{price}': {e}")

print(f"\nFinal Total: {total}")