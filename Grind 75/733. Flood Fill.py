class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        started_color = image[sr][sc]
        stack = [(sr, sc)]

        rows = len(image)
        colums = len(image[sr])
        visited = {}
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            image[cur[0]][cur[1]] = color
            if cur[0] - 1 >= 0 and image[cur[0] - 1][cur[1]] == started_color:
                stack.append((cur[0] - 1, cur[1]))

            if cur[0] + 1 < rows and image[cur[0] + 1][cur[1]] == started_color:
                stack.append((cur[0] + 1, cur[1]))

            if cur[1] - 1 >= 0 and image[cur[0]][cur[1] - 1] == started_color:
                stack.append((cur[0], cur[1] - 1))

            if cur[1] + 1 < colums and image[cur[0]][cur[1] + 1] == started_color:
                stack.append((cur[0], cur[1] + 1))
            visited[cur] = 1
        return image
