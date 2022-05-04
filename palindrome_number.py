class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy = x
        reverse_number = 0
        while copy >0:
            last_digit = copy % 10
            reverse_number = (reverse_number * 10)  + last_digit
            copy = copy // 10
        return x == reverse_number
