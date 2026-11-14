class Solution:
    def isPalindrome(self,s:str) ->bool:
        left = 0
        right = len(s)-1

        while left <=right:
            # keep moving left until your left reaches a alphnumeric character
            while left < right and not s[left].isalnum():
                left +=1
            # keep moving right until your right reaches a alphanumeric character
                while left < right and not s[right].isalnum():
                    right -=1
            # check and compare if both of them are not equal
                if s[left].lower() != s[right].lower():
                    return False

            # increment left and decrement right to reach next alphanumeric character
                left +=1
                right -=1

                return True