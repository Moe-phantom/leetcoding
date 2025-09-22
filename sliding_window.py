#dynamic window size 
s = 'abcabdabfaaa'
# l is for left pointer
l = 0 
sett = set()
n = len(s) 
longest = 0
# r is for right pointer
for r in range(n):
    while s[r] in sett:
        sett.remove(s[l])
        l += 1
    sett.add(s[r])
    ma =  r - l + 1
    #ma is the current window size
    longest = max(longest,ma)   
print(longest)

#fixed window size
def findingthemaximum(nums, k):
    cur_sum = 0 
    for i in range(k):
        cur_sum += nums[i]
    max_avg = cur_sum / k
    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, cur_sum / k)
    return max_avg

#the longest substring without repeating characters
def longestSubstring(s):
    longest = 0
    l = 0
    counter = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]] += 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
        
#leetcode 14 return the longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        i=0
        prefix = strs[0]
        for i in range(1,len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0:-1]
                if not prefix: 
                    return ""
        return prefix
        