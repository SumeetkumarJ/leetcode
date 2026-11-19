
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate elements at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # i + 1 ensures each element is used only once
                backtrack(i + 1, path, remaining - candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, [], target)
        return result
