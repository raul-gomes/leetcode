from typing import List

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

            

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[2,7,11,15], target=9))
    print(sol.twoSum(nums = [3,3], target = 6))
    print(sol.twoSum(nums = [3,2,4], target = 6))