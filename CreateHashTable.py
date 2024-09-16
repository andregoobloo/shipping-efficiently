class CreateHashTable:
    # Number of packages to set initial capacity
    NUM_OF_PACKAGES = 40

    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, capacity=NUM_OF_PACKAGES):
        # initialize the hash table with empty bucket list entries
        self.list = []
        for i in range(capacity):
            self.list.append([])

    # Inserts a new item into the hash table
    def insert(self, key, item):
        # Get the bucket list where this item will go
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Update key if it is the bucket already
        for kv in bucket_list:
            # Print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # If not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table
    # Returns the item if found, or None if not found

    def search(self, key):
        # Find the bucket list where this key is
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Search for the key in the bucket list
        for kv in bucket_list:
            # Print (key_value)
            if kv[0] == key:
                return kv[1]
        return None

    # Removes an item with matching key from the hash table.

    def remove(self, key):
        # Get the bucket list where this specific item will be removed from
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # Remove the item from the bucket list if it exists
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])