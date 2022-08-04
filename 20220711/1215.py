class Solution:
    """
    @param n: an integer
    @return: the number of '1's in the first N number in the magical string S
    """

    def switch_string(self, n: int) -> int:
        if n == 1:
            return 2
        else:
            return 1

    def magical_string(self, n: int) -> int:
        # write your code here
        if n < 3:
            return 1
        elif n == 0:
            return 0

        a = [1, 2, 2]
        left, right, value, count = 2, 2, 2, 1
        while right < n:
            if a[left] == 1:
                value = self.switch_string(value)
                a.append(value)
                right += 1
                if value == 1:
                    count += 1
            else:
                value = self.switch_string(value)
                a.append(value)
                a.append(value)
                right += 2
                if value == 1:
                    count += 2
            left += 1
        print(a)
        return count

s = Solution()
print(s.magical_string(6))
