class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(" , "]":"[" , "}":"{"}
        stack = []
        for i in s:
            if i in valid:
                top_element = stack.pop() if stack else '#'
                if valid[i] != top_element:
                    return False
            else: 
                stack.append(i)

        return not stack
            
         