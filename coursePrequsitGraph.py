class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}
        visit = set()

        for a, b in prerequisites:
            hashmap[a].append(b)

        def check(i):
            if i in visit:
                return False
            if hashmap[i] == []:
                return True

            visit.add(i)
            for tmp in hashmap[i]:
                if not check(tmp):
                    return False
            hashmap[i] = []
            visit.remove(i)
            return True

        for i in range(numCourses):
            if not check(i):
                return False

        return True


        