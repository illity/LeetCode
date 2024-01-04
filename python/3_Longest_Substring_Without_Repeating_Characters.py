class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = ''
        longest = ''
        for i in range(len(s)):
            print(i, current)
            if not s[i] in current:
                current += s[i]
                if len(current) > len(longest):
                    longest = current
            else:
                current = s[i-len(current)+1+current.index(s[i]):i+1]
        return len(longest)

print('3=', Solution().lengthOfLongestSubstring('dvdf'))
print('6=', Solution().lengthOfLongestSubstring('bbtablud'))
print('3=', Solution().lengthOfLongestSubstring('pwwkew'))
