class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.entries = entries
        self.buckets = buckets
        self.table = [None] * entries

    def hash_function(self, key):
        return hash(key) % self.entries

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def lookup(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

# Example usage
hash_table = DLeftHashTable(10, 5)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)

print(hash_table.lookup("apple"))  # Output: 10
print(hash_table.lookup("banana")) # Output: 20
print(hash_table.lookup("grape"))  # Output: None

# reference: chatGPT