from typing import List


class Solution:
    @staticmethod
    def reduce_shift(shifts: List[List[int]]) -> List[int]:
        right_shift = 0
        left_shift = 0
        for shift in shifts:
            if shift[0]:
                right_shift += shift[1]
            else:
                left_shift += shift[1]

        if right_shift > left_shift:
            return [1, right_shift - left_shift]
        else:
            return [0, left_shift - right_shift]

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift_by = self.reduce_shift(shift)
        shift_pos = shift_by[0]
        shift_num = shift_by[1] % len(s)
        str_arr = list(s) if shift_pos == 1 else list(s[::-1])

        steps = 0
        start = 0

        while steps < len(s):
            index = start
            current_num = str_arr[start]

            while True:
                next_index = (index + shift_num) % len(s)
                current_num, str_arr[next_index] = str_arr[next_index], current_num
                index = next_index
                steps += 1

                if start == index:
                    break

            start += 1

        return ''.join(str_arr if shift_pos == 1 else str_arr[::-1])


class Solution2:
    @staticmethod
    def reduce_shift(shifts: List[List[int]]) -> int:
        shift = 0
        for x, y in shifts:
            if x:
                shift += y
            else:
                shift -= y

        return shift

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = self.reduce_shift(shift) % len(s)
        return s[-move:] + s[:-move]
        # print(move)


sol = Solution2()
shifts = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]
print('Shifted', sol.stringShift('xqgwkiqpif', shifts))
