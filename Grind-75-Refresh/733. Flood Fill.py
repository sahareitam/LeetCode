class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        def dfs(start_pix_color, image, sr, sc, color):
            if sc < 0 or sc >= len(image[0]) or sr < 0 or sr >= len(image) or (start_pix_color != image[sr][sc]):
                return
            image[sr][sc] = color
            dfs(start_pix_color, image, sr + 1, sc, color)
            dfs(start_pix_color, image, sr - 1, sc, color)
            dfs(start_pix_color, image, sr, sc + 1, color)
            dfs(start_pix_color, image, sr, sc - 1, color)
            return image
        return dfs(image[sr][sc], image, sr, sc, color)