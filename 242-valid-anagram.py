class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sorted_s = "".join(sorted(list(s)))
            sorted_t = "".join(sorted(list(t)))
            return sorted_s == sorted_t


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
