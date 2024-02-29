class Solution:
    def findItinerary(self, tickets: [[]]) -> []:

        adjList = { src:[] for src, dist in tickets }
        result = []
        for src, dist in tickets:
            adjList[src].append(dist)

        for key in adjList:
            adjList[key].sort()

        def dfs(src):
            if src in adjList:
                temp = adjList[src][:]
                while temp:
                    v = temp[0]
                    adjList[src].pop(0)
                    dfs(v)
                    temp = adjList[src][:]

            result.append(src)


        dfs("JFK")
        if len(result) != len(tickets) + 1:
            return []
        result.reverse()
        return result
