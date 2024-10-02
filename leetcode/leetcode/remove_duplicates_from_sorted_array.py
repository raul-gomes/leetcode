from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indexes = []
        size = len(nums)
        for i in range(size):
            for j in range(i + 1 , size):
                  
                if (nums[i] == nums[j]):
                    indexes.append(j)
        
        indexes = list(set(indexes))
        indexes.sort(reverse=True)

        for i in indexes:
            del nums[i]
            nums.append('_')
            
        return size - len(indexes), nums
        
        
if __name__ == '__main__':
    test = Solution()
    print(test.removeDuplicates([1,1,2]))
    print(test.removeDuplicates([1,2,2]))
    print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))