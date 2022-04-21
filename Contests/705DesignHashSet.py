# https://leetcode.com/problems/design-hashset/
# https://leetcode.com/problems/design-hashset/discuss/1968265/Python-6-Simple-Approaches-with-Explanation


class MyHashSet:
    BUCKET_SIZE = 256  # can be any number

    def __init__(self):
        self.hs = [[] for _ in range(self.BUCKET_SIZE)]  # list of BUCKET_SIZE 'buckets'

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.curr.append(key)  # add key to appropriate bucket

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.curr.remove(key)  # remove key from appropriate bucket

    def contains(self, key: int) -> bool:
        self.curr = self.hs[key % self.BUCKET_SIZE]  # key % self.BUCKET_SIZE is a simple hashing function
        return key in self.curr  # self.curr is a 'static' variable representing the current bucket

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)