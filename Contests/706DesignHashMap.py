# https://leetcode.com/problems/design-hashmap/
# https://leetcode.com/problems/design-hashmap/discuss/1970885/Python-Basic-HashTable-implementation

class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)
        else:
            print("key () not in MyHashMap".format(
                key
            ))

# If you know how HashTable works then it should be an easy problem. I believe that as a Software Engineer, understanding how HashTable works is a compulsory.
#
# To build HashTable, we need buckets as an static array to store list of pairs (key, value) which has the same bucket index:
# The bucket index = hash_code(key) % BUCKET_SIZE
# The larger BUCKET_SIZE is, the low chance collision happens.
# To get a hash code of a integer value, we can use their value directly. But for other type like String, Object,...
# we need to write an efficient hash function to get the hash code which causes as low collision as possible.
# For different keys but share the same bucket index, we can store pair of (key, value) as a list or Balanced BST:
# If store as a list, in the worst case, it will cost O(N) for put, get, remove opertions, where N is number of keys in the same bucket.
# Here I choose to implement this way since it's easy to implement.
# If store as a Balanced BST, in the worst case, it will cost O(logN) for put, get, remove operations, where N is number of keys in the same bucket.

class MyHashMap1:

    def __init__(self):
        self.BUCKET_SIZE = 1000
        self.buckets = [[] for _ in range(self.BUCKET_SIZE)]  # bucket[i] stores list of (key, value)

    def getBucket(self, key):
        return self.buckets[key % self.BUCKET_SIZE]

    def findKey(self, bucket, key):
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findKey(bucket, key)
        if nodeIndex != -1:
            bucket[nodeIndex][1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.getBucket(key)
        nodeIndex = self.findKey(bucket, key)
        if nodeIndex == -1: return -1
        return bucket[nodeIndex][1]

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findKey(bucket, key)
        if nodeIndex == -1: return
        del bucket[nodeIndex]