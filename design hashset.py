class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key):
        self.data[key] = True

    def remove(self, key):
        self.data[key] = False

    def contains(self, key):
        return self.data[key]
