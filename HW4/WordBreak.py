"""
time complexity: O(n^3), n- len of string
space complexity: O(n)
time spent: 40 minutes
approach: copy the Trie, add all the words in to a trie. Use DP to put all the valid word into the array.
if the last item in the DP array is not True(meaning a word can be created) return False, bc then it does not create
an word without using some letter

"""


class TrieNode:
    def __init__(self, value):
        self.root = value
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]
        current.isEnd = True

    def valid(self, word):

        current = self.root

        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.isEnd

def word_break(string, dictt):
    n = len(string)
    dp = []
    trie = Trie()

    for i in dictt:
        trie.insert(i)

    for i in range(n+1):
        dp.append(False)

    dp[0] = True

    for i in range(1, len(dp)):
        for j in range(i):
            #print(input_str[j:i])
            if dp[j] and trie.valid(string[j:i]):
                dp[i] = True
                break
    #print(dp)
    return dp[n]


words = ["elf", "go", "golf", "man", "manatee", "not", "note", "pig", "quip", "tee", "teen"]

print(word_break("mangolf", words))  # Outputs: True
print(word_break("manateenotelf", words))  # Outputs: True
print(word_break("quipig", words))  # Outputs: False
