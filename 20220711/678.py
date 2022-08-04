class Solution:
    """
    @param str: String
    @return: String
    """

    def shortest_palindrome(self, str: str) -> str:
        # Write your code here
        left, right, begin = 0, len(str) - 1, 0
        while left <= right: # and left + 1 != right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else:
                left = 0
                begin += 1
                right = len(str) - 1 - begin

        # if left + 1 == right and str[left] != str[right]:
        #     begin += 3
        for i in range(begin):
            str = str[len(str) - begin + i] + str
            # if left == right and (left + 1 == right and str[left] == str[right]):
            # else:
            #     str = str[len(str) - begin  + i] + str
        print(begin)
        return str


a = "aaeeeaaa"
a = "abcd"
a = 'sdsdlkjsaoio'
a = "aaeeaaa"
a = "aaaa"
# a = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
a = "abcabcabc"
a = "abcdefghijklmnopqrstuvwxyz"
s = Solution()
print(s.shortest_palindrome(a))
