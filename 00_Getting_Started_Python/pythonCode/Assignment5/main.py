import math_utils
from math_utils import add, divide
from string_utils import capitalize_words, reverse_string, word_count
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print("Addition", add(10, 20))
print("Division", divide(10, 20))
print("Subtraction", math_utils.subtract(10, 20))
print("Multiplication", math_utils.multiply(10, 20))
print("Division", math_utils.divide(10, 20))
print("Square", math_utils.square(10))
print("Cube", math_utils.cube(10))



print(capitalize_words("hello world"))
print(reverse_string("hello world"))
print(word_count("hello world"))

print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))