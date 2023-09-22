class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        m = len(image)    # Number of rows
        n = len(image[0]) # Number of columns
        original_color = image[sr][sc]
        if original_color == color:
            return image  # No need to fill if the original color and new color are the same
        
        queue = [(sr, sc)]
        while queue:
            u = queue.pop(0)
            image[u[0]][u[1]] = color
            for i, j in zip(di, dj):
                vi = u[0] + i
                vj = u[1] + j
                if 0 <= vi < m and 0 <= vj < n and image[vi][vj] == original_color:
                    queue.append((vi, vj))
        return image

