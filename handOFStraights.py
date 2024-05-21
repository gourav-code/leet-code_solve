class Solution:
    def isNStraightHand(self, hand: [int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False

        count = {}
        for tmp in hand:
            count[tmp] = 1+count.get(tmp,0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]

            for tmp in range(first, first+groupSize):
                if tmp not in count:
                    return False

                count[tmp] -= 1
                if count[tmp] == 0:
                    if tmp != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True