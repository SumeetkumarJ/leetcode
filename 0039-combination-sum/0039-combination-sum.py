
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Same index allows reuse of the candidate
                backtrack(i, path, remaining - candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, [], target)
        return result
