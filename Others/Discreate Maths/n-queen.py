import itertools as it


class NQueenBruteForceSolution:
    @staticmethod
    def is_solution(perm: tuple):
        for (i, j) in it.combinations(perm, 2):
            if abs(i - j) == abs(perm[i] - perm[j]):
                return False

        return True

    def find_solution(self, num):
        for perm in it.permutations(range(num)):
            if self.is_solution(perm):
                return perm
                # exit()


class NQueenBackTrackSolution:
    @staticmethod
    def has_no_conflict(perm):
        i = len(perm) - 1
        for j in range(i):
            if i - j == abs(perm[i] - perm[j]):
                return False
        return True

    def _generate_permutation(self, perm, n):
        if len(perm) == n:
            print(perm, NQueenBruteForceSolution.is_solution(perm))
            exit()

        for k in range(n):
            if k not in perm:
                perm.append(k)
                if self.has_no_conflict(perm):
                    self._generate_permutation(perm, n)
                perm.pop()

    def find_solution(self, n):
        return self._generate_permutation([], n)


sol = NQueenBackTrackSolution()
print(sol.find_solution(20))
