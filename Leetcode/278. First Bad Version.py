bad_version = 3


def isBadVersion(num):
    if num >= bad_version:
        return True

    return False


class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1


sol = Solution()
print(sol.firstBadVersion(100))
