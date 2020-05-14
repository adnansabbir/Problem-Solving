class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for i, char in enumerate(word):
            if char not in trie:
                trie[char] = {}
                trie[char]['end'] = i == len(word) - 1
            else:
                trie[char]['end'] = i == len(word) - 1 or trie[char]['end']
            trie = trie[char]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return trie['end']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('')
obj.insert('adnan')
obj.insert('sakib')
print(obj.trie)
print(obj.startsWith('adnaa'))

# a = {
#     'b': {'c': 'c'}
# }
# print(a)
#
# a = a['b']
# print(a)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
