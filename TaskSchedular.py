from collections import Counter
def leastInterval(self, tasks: List[str], n: int) -> int:
    c = Counter(tasks)
    l = [-tmp for tmp in c.values()]
    heapq.heapify(l)

    q=deque()
    time=0
    while l or q:
        time += 1
        if l:
            tmp = 1 + heapq.heappop(l)
            if tmp:
                q.append([tmp, time+n])
        if q and q[0][1] == time:
            temp1, temp2 = q.popleft()
            heapq.heappush(l, temp1)

    return time
