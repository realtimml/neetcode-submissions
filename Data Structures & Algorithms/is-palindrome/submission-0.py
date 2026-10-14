class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_alpha_num = ""
        for c in s:
            if (c.isalnum()):
                no_alpha_num += c.lower()
        print(no_alpha_num)

        return no_alpha_num == no_alpha_num[::-1]