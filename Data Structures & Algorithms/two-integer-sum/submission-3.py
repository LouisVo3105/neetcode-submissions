class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}  

        for i, n in enumerate(nums):
            H[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff  in H and H[diff] != i:
                return [i,H[diff]]
        return []