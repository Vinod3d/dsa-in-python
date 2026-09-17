products = ["Laptop", "Phone", "Headphones"]

prices = {
    "Laptop": 80000,
    "Phone": 30000,
    "Headphones": 5000
}

categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Headphones": "Audio"
}

catalog = [
    (product, prices[product], categories[product]) for product in products
]

print(catalog)


category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)

max_category = max(
    category_to_products,
    key=lambda category: len(category_to_products[category])
)

print("Category:", max_category)
print("Products:", category_to_products[max_category])