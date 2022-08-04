class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def character_replacement(self, s: str, k: int) -> int:
        # write your code here
        # if not s or len(s) == 0:
        #     return 0
        # res, left, right = 0, 0, 1
        # left_count, right_count = 1, 1
        # while right < len(s):
        #     if s[left] == s[left + 1] and left <= k:
        #         left += 1
        #         right += 1
        #         left_count += 1
        #     elif s[right] == s[right + 1]:
        #         right += 1
        #         right_count += 1
        # return left_count + right_count
        # num = [0] * 26
        # n = len(s)
        # maxn = left = right = 0
        #
        # while right < n:
        #     num[ord(s[right]) - ord("A")] += 1
        #     maxn = max(maxn, num[ord(s[right]) - ord("A")])
        #     if right - left + 1 - maxn > k:
        #         num[ord(s[left]) - ord("A")] -= 1
        #         left += 1
        #     right += 1
        #
        # return right - left
        # Given        a        string        that        consists        of        only
        # uppercase        English        letters, you        can        replace        any
        # letter in the        string
        # with another letter at most k times.Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
        counter = {}
        answer = 0
        j = 0
        # maxFreq 以打擂台的方式记录出现最多的字符数量
        max_freq = 0
        for i in range(len(s)):
            # 当j作为下标合法 且 最少需要被替换的字母数目<=k
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                # 更新出现最多的字符数量
                max_freq = max(max_freq, counter[s[j]])
                j += 1

            # 如果替换 除出现次数最多的字母之外的其他字母 的数目>k,
            # 说明有一个不能换，答案与j-i-1进行比较；
            # 否则说明直到字符串末尾替换数目都<=k，可以全部换掉
            # 答案与子串长度j-i进行比较
            if j - i - max_freq > k:
                answer = max(answer, j - 1 - i)
            else:
                answer = max(answer, j - i)

            # 起点后移一位，当前起点位置的字母个数-1
            counter[s[i]] -= 1
        return answer


# "AABABBA"
a = 'AABABBA'
s = Solution()
print(s.character_replacement(a, 2))
