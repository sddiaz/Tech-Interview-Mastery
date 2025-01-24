# Data Structure: HashMap (or Hash Table)

## 1. Definition
A **HashMap** is a data structure that stores key-value pairs. It allows for fast access to values via keys using a hashing function.  
The primary operations are **insert**, **lookup**, and **delete**, typically with average time complexity of **O(1)**.

## 2. Core Concepts
- **Key-Value Pairs**: Data is stored as a combination of keys and their associated values.
- **Hashing Function**: A function that converts a key into an index in an array, where the key-value pair is stored.
- **Collision**: When two different keys hash to the same index, a **collision** occurs.

## 3. How It Works
- A **hashing function** is applied to the key to determine the index of the array where the value should be stored.
- If the index is already occupied (collision), a **collision resolution** strategy is applied:
    - **Chaining**: Store a list (or another collection) at each array index to handle multiple key-value pairs.
    - **Open Addressing**: If a collision occurs, search for the next available slot using a probing technique.

## 4. Key Operations
- **Insert (Put)**: Add a key-value pair to the hashmap. If the key already exists, update the value.
- **Lookup (Get)**: Retrieve the value associated with a key. If the key does not exist, return `None` (or similar).
- **Delete (Remove)**: Remove the key-value pair associated with a specific key.

## 5. Time Complexity
- **Average Case**:
    - Insert: **O(1)**
    - Lookup: **O(1)**
    - Delete: **O(1)**
- **Worst Case** (with poor hashing or too many collisions):
    - Insert: **O(n)**
    - Lookup: **O(n)**
    - Delete: **O(n)**
- **Resizing/Reshaping**: When the table becomes too full (e.g., load factor exceeds a threshold), the table may be resized and rehashed.

## 6. Collision Resolution Strategies
- **Chaining**: Each index of the table holds a list of key-value pairs. This allows multiple keys to hash to the same index without affecting other operations.
- **Open Addressing**: Use probing to find the next available spot:
    - **Linear Probing**: Search sequentially for the next available slot.
    - **Quadratic Probing**: Use a quadratic function to search for the next available slot.
    - **Double Hashing**: Use a second hash function to calculate the probe sequence.

## 7. When to Use
- **Fast Lookups**: When you need quick retrieval of data via unique keys.
- **When the Key Set is Known**: Ideal when you know the keys ahead of time (e.g., looking up user profiles by user ID).

## 8. Limitations
- **Collisions**: Poor hash functions or excessive collisions can degrade performance.
- **Memory Usage**: HashMaps may use more memory than other data structures (e.g., arrays or linked lists) due to the underlying array and handling collisions.

## 9. Example Code
A simple example of a **HashMap** implementation with chaining.

```python
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Chaining using lists

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        for idx, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][idx] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def remove(self, key):
        index = self.hash_function(key)
        for idx, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][idx]
                return
        return None  # Key not found

# Example usage:
hashmap = HashMap()
hashmap.put("apple", 10)
hashmap.put("banana", 20)
print(hashmap.get("apple"))  # 10
hashmap.remove("banana")
print(hashmap.get("banana"))  # None