class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str_x = str(x)
        len_x = len(str_x)
        for i in range(int(len_x)):
            if str_x[i] != str_x[len_x-1-i]:
                return False
        return True
