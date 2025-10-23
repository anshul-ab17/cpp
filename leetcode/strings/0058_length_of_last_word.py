# LC 58. Length of Last Word | Easy
class Solution:
    def lengthOfLastWord_pythonic(self, s):
        return len(s.split()[-1])

    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == ' ': i -= 1
        j = i
        while j >= 0 and s[j] != ' ': j -= 1
        return i - j
