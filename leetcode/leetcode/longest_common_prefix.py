"""
14. Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

       if len(strs) == 1:
            return strs[0]
        ret = ''
        test = bool
        
        strs.sort(key=len, reverse=False)
        
        base = strs[0]
        for i in range(len(base)):
            test = False
            for word in strs[1:]:
                if word[i] == base[i]:
                    test = True
            
            if test:
                ret += base[i]
                
        return ret
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs or strs == []:
            return ""
        
        preix = strs[0]
        for i in range(1,len(strs)):
            while(preix != ""):
                try:
                    if str.index(str(strs[i]),preix) == 0:
                        break
                    else:
                        preix = preix[:-1]
                        print(preix)
                except:    
                    preix = preix[:-1]
        return preix

        
if __name__ == '__main__':
    longest = Solution()
    print(longest.longestCommonPrefix(["flower","flow","flight"]))
    print(longest.longestCommonPrefix(["reflower","flow","flight"]))
    print(longest.longestCommonPrefix(["a"]))
    print(longest.longestCommonPrefix(["ab", "a"]))
    print(longest.longestCommonPrefix(["flower","flower","flower","flower"]))