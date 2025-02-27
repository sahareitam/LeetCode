class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        hash_count = {}
        dep_map = {}
        for i in range(numCourses):
            hash_count[i] = 0
            dep_map[i] = []

        for c in prerequisites:
            hash_count[c[0]] += 1
            dep_map[c[1]].append(c[0])

        queue = deque()
        for i in range(numCourses):
            if hash_count[i] == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            for d in dep_map[cur_course]:
                hash_count[d] -= 1
                if hash_count[d] == 0:
                    queue.append(d)

        for i in range(numCourses):
            if hash_count[i] > 0:
                return False
        return True



