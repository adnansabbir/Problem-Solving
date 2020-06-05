from random import choices
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        return choices(range(len(self.w)), weights=self.w, k=1)[0]
