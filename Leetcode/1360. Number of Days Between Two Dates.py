from _datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        start = datetime.strptime(date1, '%Y-%m-%d')
        end = datetime.strptime(date2, '%Y-%m-%d')

        return abs((end - start).days)


sol = Solution()
print(sol.daysBetweenDates('2020-01-15', '2019-12-31'))
