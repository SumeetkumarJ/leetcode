
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            # A complete permutation is formed
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                # Choose
                nums[start], nums[i] = nums[i], nums[start]

                # Explore
                backtrack(start + 1)

                # Undo choice
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
