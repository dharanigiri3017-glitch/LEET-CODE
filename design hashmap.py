class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size

        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.map[index].append([key, value])

    def get(self, key):
        index = key % self.size

        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        index = key % self.size

        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                self.map[index].pop(i)
                return
