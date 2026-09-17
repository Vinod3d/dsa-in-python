## 1. From products list, create a set of categories called categories_set (if product names do not contain categories, create a short parallel list categories = [..] with matching length and use that.)


categories = [
    "Electronics",
    "Electronics",
    "Furniture",
    "Accessories",
    "Electronics",
    "Accessories",
    "Wearables",
    "Audio",
]

categories_set = set(categories)

print(categories_set)

## 2. Demonstrate adding a new category to the set and show that duplicates are ignored.

categories_set.add("Home Appliances")
print("After adding new category:", categories_set)

categories_set.add("Electronics")
print("After attempting duplicate:", categories_set)

## 3. Check whether a category exists

print(categories_set._hash__("Electronics"))
print(categories_set._hash__("Sports"))

## 4. Get the total number of unique categories (using len())
total_unique = len(categories_set)
print("Total number of unique categories:", total_unique)