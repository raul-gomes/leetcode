from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        other_list = []
        
        for i, num in enumerate(nums):
            if num != val:
                other_list.append(nums[i])
        
        return len(other_list)
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums=[3,2,2,3], val=3))
    print(sol.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
    
    