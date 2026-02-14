class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size
    
    def add(self, value):
        index = self.hash_function(value)
        if value not in self.buckets[index]:
            self.buckets[index].append(value)
        else:
            print(f"{value} already exists in the hash table.")
    
    def contains(self, value):
        index = self.hash_function(value)
        return value in self.buckets[index]
    
    def remove(self, value):
        index = self.hash_function(value)
        if value in self.buckets[index]:
            self.buckets[index].remove(value)
        else:
            print(f"{value} not found in the hash table.")

    def print_set(self):
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


hash_set = SimpleHashTable(size=10)

hash_set.add("apple")
hash_set.add("banana")
hash_set.add("orange")
hash_set.print_set()
print(hash_set.contains("banana"))  # Output: True
print(hash_set.contains("grape"))   # Output: False
hash_set.remove("banana")
print(hash_set.contains("banana"))  # Output: False
hash_set.print_set()