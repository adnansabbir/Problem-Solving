from typing import List
import collections


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N <= 2 or not dislikes:
            return True

        NO_COLOR, BLUE, RED = 0, 1, -1

        color_table = [NO_COLOR] * (N + 1)
        dislike_table = collections.defaultdict(list)

        def dislikesAreDifferentColor(person, color):
            color_table[person] = color

            for other_person in dislike_table[person]:
                if color_table[other_person] == color:
                    return False
                elif color_table[other_person] == NO_COLOR and (not dislikesAreDifferentColor(other_person, -color)):
                    return False
            return True

        for p1, p2 in dislikes:
            dislike_table[p1].append(p2)
            dislike_table[p2].append(p1)

        for person in range(1, N + 1):
            if color_table[person] == NO_COLOR and (not dislikesAreDifferentColor(person, BLUE)):
                return False

        return True
