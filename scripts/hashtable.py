#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    # In all cases: quadratic time, O(n^2)
    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []                          # O(1)
        for bucket in self.buckets:            # O(n)
            for key, value in bucket.items():  # O(n)
                all_keys.append(key)           # O(1)
        return all_keys                        # O(1)

    # In all cases: quadratic time, O(n^2)
    def values(self):
        """Return a list of all values in this hash table"""
        items = []                             # O(1)
        for bucket in self.buckets:            # O(n)
            for key, value in bucket.items():  # O(n)
                items.append(value)            # O(1)
        return items                           # O(1)

    # Worst case: quadratic time, O(n^2)
    # Best case: linear time, O(n)
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []                        # O(1)
        for bucket in self.buckets:           # O(n)
            all_items.extend(bucket.items())  # O(n)
        return all_items                      # o(1)

    # In all cases: linear time, O(n)
    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        length = 0                     # O(1)
        for bucket in self.buckets:    # O(n)
            length += bucket.length()  # O(1)
        return length                  # O(1)

    # Worst case: quadratic time, O(n^2)
    # Best case: linear time, O(n)
    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        if key in self.keys():  # O(n + n^2)
            return True         # O(1)
        return False            # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        index = self._bucket_index(key)                                      # O(1)
        found_value = self.buckets[index].find(lambda item: item[0] == key)  # O(1 + n)
        if found_value:                                                      # O(1)
            return found_value[1]                                            # O(1)
        raise KeyError("Can not find key {} to get value".format(key))       # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        index = self._bucket_index(key)                # O(1)
        bucket = self.buckets[index]                   # O(1)
        old_data = bucket.find(lambda x: x[0] == key)  # best: O(1), worst: O(n)

        if old_data:                                   # O(1)
            bucket.replace(old_data, (key, value))     # best: O(1), worst: O(n)
        else:
            bucket.append((key, value))                # O(1)

    # Worst case: linear time, O(n)
    # Best case: constant time, O(1)
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        index = self._bucket_index(key)                   # O(1)
        bucket = self.buckets[index]                      # O(1)
        found = bucket.find(lambda item: item[0] == key)  # best: O(1), worst: O(n)

        if found:                                         # O(1)
            bucket.delete(found)                          # best: O(1), worst: O(n)
        else:
            raise KeyError("Can not find key {} to delete value".format(key))  # O(1)


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
