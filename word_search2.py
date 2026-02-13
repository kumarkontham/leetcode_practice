class Trie_node:
    def __init__(self):
        self.hashmap = {}
        self.isend = False
class wordsearch:
    #words = ["oath","pea","eat","rain"]
    #board = [["o","a","a","n"],
    #         ["e","t","a","e"],
    #         ["i","h","k","r"],
    #         ["i","f","l","v"]]
    def search_words(self,words,board):
        trie_node = Trie_node()
        for word in words:
            curr = trie_node
            for char in word:
                if char not in trie_node.hashmap:
                    curr.hashmap[char] = Trie_node()
                curr= curr.hashmap[char]
            curr.isend = True
        visit = set()
        res = set()
        def dfs(i,j,node,word):
            if node.isend:
                return res.add(word)
            if i<0 or j<0 or i>len(board)-1 or j>len(board[0])-1 or board[i][j] not in node.hashmap or (i,j) in visit:
                return 
            if board[i][j] in node.hashmap:
                node = node.hashmap[board[i][j]]
                word+=board[i][j]
                visit.add((i,j))
                dfs(i,j+1,node,word)
                dfs(i,j-1,node,word)
                dfs(i+1,j,node,word)
                dfs(i-1,j,node,word)
                visit.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,trie_node,"") 
        return list(res)
obj = wordsearch()
words = ["oath","pea","eat","rain"]
board = [["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]]
print(obj.search_words(words,board))


