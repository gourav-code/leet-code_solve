class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adajcent = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adajcent[w1[j]].add(w2[j])
                    break

        visit = {} #visit:False, inCurrent_path = True
        result = []
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for tmp in adajcent[c]:
                if dfs(tmp):
                    return True

            visit[c] = False
            result.append(c)

        for tmp in adajcent:
            if dfs(tmp):
                return ""

        result.reverse()
        return "".join(result)
