"""

Code
Testcase
Testcase
Test Result
13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

from itertools import groupby
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
            }
        inteiro = 0
        
        tamanho = len(s)
        
        for i in range(tamanho):
            
            if i + 1 < tamanho and roman_number[s[i]] < roman_number[s[i + 1]]:
                inteiro -= roman_number[s[i]]
            else:
                inteiro += roman_number[s[i]]

        return inteiro

    # def splitString(self, s: str) -> List[str]:
    #     return [''.join(g) for _, g in groupby(s)]
    
    # def convertToNumber(self, s: List[str]) -> List[int]:
    #     roman_number = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000,
    #         }
        
    #     total = []
    #     test = 0
    #     for char in s:
    #         if len(char) > 1:
    #             for x in char:
    #                 test += roman_number[x]
    #             total.append(test)
    #             continue
    #         total.append(roman_number[char])
            
    #     return total

if __name__ == '__main__':
    roman = Solution()
    print(roman.romanToInt('MCMXCIV'))
    print(roman.romanToInt('IV'))