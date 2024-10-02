class Solution:
    def isValid(self, s: str) -> bool:
        
        checked = ['(', '{', '[']
        valid = {'(': ')', '{': '}', '[':']'}
        
        open_string = []
        for p in s:
            if p in checked:
                open_string.append(p)
            else:
                if len(open_string) > 0:
                    test = open_string.pop()
                else:
                    return False
                
                if p != valid[test]:
                    return False
        
        if not open_string:
            return True
        else:
            return False
        
    


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("([])"))
    print(s.isValid("]"))
                
        