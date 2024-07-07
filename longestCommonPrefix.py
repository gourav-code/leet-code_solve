class Solution:
    def longestCommonPrefix(self, n, arr):
        # code here
        arr = sorted(arr)
        start = arr[0]
        end = arr[len(arr)-1]
        ans = ''
        for i in range(min(len(start), len(end))):
            if start[i] != end[i]:
                break
            ans += start[i]
            
        if len(ans) == 0:
            return '-1'
        
        return ans

#----------------------------------------------------------------------------------------------
#second best solution
#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
        
    def addWord(self, word):
        cur = self
        
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            
        cur.endofWord = True
        
#second 
class Solution2:
    def longestCommonPrefix(self, n, arr):
        # code here
        root = TrieNode()
        for tmp in arr:
            root.addWord(tmp)
            
        ans = ''
        i = 0
        while len(root.children) == 1 and i < len(arr[0]):
            ans += arr[0][i]
            root = root.children[arr[0][i]]
            if root.endofWord:
                break
            i += 1
        
        if len(ans) == 0:
            return '-1'
        
        return ans