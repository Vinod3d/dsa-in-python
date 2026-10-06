try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator

except ValueError:
    print("Error: Input must be a valid number.")

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

else:
    print(f"Result: {result}")

finally:
    print("Operation Complete")