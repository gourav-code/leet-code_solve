class Solution:
    def partitionLabels(self, s: str) -> [int]:
        lastIndex = {}
        for i,tmp in enumerate(s):
            lastIndex[tmp] = i

        output = []
        size, end = 0,0

        for i, tmp in enumerate(s):
            size += 1
            end = max(end, lastIndex[tmp])

            if i == end:
                output.append(size)
                size = 0

        return output