from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixels = [[sr, sc]]
        image_width = len(image[0])
        image_height = len(image)
        pixel_color = image[sr][sc]

        if newColor == pixel_color: return image

        while starting_pixels:
            sr_p, sc_p = starting_pixels.pop()
            image[sr_p][sc_p] = newColor
            # visited_pixels[sr_p][sc_p] = True

            if 0 <= sc_p - 1 < image_width and image[sr_p][sc_p - 1] == pixel_color:
                starting_pixels.append([sr_p, sc_p - 1])
            if 0 <= sc_p + 1 < image_width and image[sr_p][sc_p + 1] == pixel_color:
                starting_pixels.append([sr_p, sc_p + 1])

            if 0 <= sr_p - 1 < image_height and image[sr_p - 1][sc_p] == pixel_color:
                starting_pixels.append([sr_p - 1, sc_p])
            if 0 <= sr_p + 1 < image_height and image[sr_p + 1][sc_p] == pixel_color:
                starting_pixels.append([sr_p + 1, sc_p])

        return image


sol = Solution()
image = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
]
image = [
    [0, 0, 0],
    [0, 1, 1]]
sr = 1
sc = 1
new_color = 2
for r in sol.floodFill(image, sr, sc, new_color):
    print(r)
