class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        students = deque(students)
        sandwiches = deque(sandwiches)
        while count < len(students) and len(sandwiches) != 0:
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                students.popleft()
                count = 0
            else:
                count+=1
                std = students.popleft()
                students.append(std)
        return len(sandwiches)