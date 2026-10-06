cart = []

while True:
    user_input = input("Enter price (or 'q' to stop): ").strip()

    if user_input.lower() == "q":
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Price cannot be negative.")

        cart.append(price)
        print(f"Added {price:.2f} to cart.")

    except ValueError as e:
        print(f"Invalid input: {e}")

print("\n--- Cart Summary ---")
print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart):.2f}")