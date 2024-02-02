class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:

        if endWord not in wordList:
            return 0

        neighbor = collections.defaultdict(list) #it makes sure that for any key starts with empty list
        wordList.append(beginWord)

        for word in wordList:
            for tmp, a in enumerate(word):
                pattern = word[:tmp] + "*" + word[tmp + 1:]
                neighbor[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            for tmp in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for temp, a in enumerate(word):
                    pattern = word[:temp] + "*" + word[temp + 1:]
                    for words in neighbor[pattern]:
                        if words not in visit:
                            visit.add(words)
                            q.append(words)
            result += 1
        return 0


