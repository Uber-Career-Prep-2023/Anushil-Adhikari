"""
time spent: 40 minutes
time complexity: O((len(arr) * len*arr[0])^len(word))
space complex: O(len(arr) * len*arr[0])
approach: I decided to add all the words from the dictinary to my trie, then I did a dfs method from each box in
the board. In my dfs method I added it to a visit array and also checked if its a word in my trie, if it is I added
it to the final array, if not I looped through all the directions, and check if any of them are a child to
current.child if they are I did the dfs method again with the new info and repeat until the loop stops. finally I remove
the points I added to visit so when it runs again from another box, it wont give me an issue.
"""


class TrieNode:
    def __init__(self, value):
        self.root = value
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, value):
        current = self.root

        for letter in value:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)

            current = current.children[letter]
        current.isEnd = True

    def isValidWord(self, word):

        if word == "":
            return False

        current = self.root

        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]

        if not current.isEnd:
            return False

        return True


def boggle(dictt, board):
    trie = Trie()
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    for i in dictt:
        trie.insert(i)

    final = set()
    current = trie.root
    visit = set()

    def dfs(x, y, current, word):
        visit.add((x, y))

        if trie.isValidWord(word):
            final.add(word)

        for i, u in direction:
            newR, newC = i + x, u + y
            if 0 <= newR < len(board) and 0 <= newC < len(board[0]) and (newR, newC) not in visit:
                if board[newR][newC] in current.children:
                    dfs(newR, newC, current.children[board[newR][newC]], word + board[newR][newC])
        visit.remove((x, y))

    for i in range(len(board)):
        for u in range(len(board[i])):
            if board[i][u] in current.children:
                dfs(i, u, current.children[board[i][u]], board[i][u])

    return final


temp = ["ace", "ape", "cape", "clap", "clay", "rap", "ray", "tap", "gape", "grape", "lace", "lap", "lay", "tape",
        "trace", "trap", "mace", "map", "may", "pace", "pay", "tray", "yap"]
board = [["a", "d", "e"], ["r", "c", "p"], ["l", "a", "y"]]

print(boggle(temp, board))
