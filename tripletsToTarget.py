class Solution:
    def mergeTriplets(self, triplets: [[int]], target: [int]) -> bool:
        good = set()

        for tmp in triplets:
            if tmp[0] > target[0] or tmp[1] > target[1] or tmp[2] > target[2]:
                continue

            for i,val in enumerate(tmp):
                if val == target[i]:
                    good.add(i)

        return len(good) == 3