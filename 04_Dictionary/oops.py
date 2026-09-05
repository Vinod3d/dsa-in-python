# class Animal:
#     def show(self):
#         print("hello from india")

# class Dog(Animal):
#     def show(self):
#         print("hello from bhopal")
#         super().show()

# a = Dog()
# a.show()


def even(x):
    if x%2 == 0:
        return True
    else:
        return False 


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(even, a)))