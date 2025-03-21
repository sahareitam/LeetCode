class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) <= 1:
            return asteroids

        stack = [asteroids[0]]
        a = 1
        while a < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[a] < 0:
                if stack[-1] > abs(asteroids[a]):
                    a += 1
                    continue
                elif stack[-1] < abs(asteroids[a]):
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    a += 1
                    continue
            stack.append(asteroids[a])
            a += 1

        return stack


