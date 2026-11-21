
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []
        path = []
        visited = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                # Skip duplicate permutations
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                visited[i] = False

        backtrack()
        return result
