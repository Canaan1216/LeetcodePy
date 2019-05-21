# -*- coding:utf-8 -*-
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
示例1:
输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3

示例2:
输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为1

示例 3:
输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 # 存储历史循环中最长的子串长度
        if s is None or len(s) == 0:
            return res
        d = {}
        # 定义字典存储不重复的字符和字符所在的下标
        tmp = 0
        # 存储单次循环中的最长子串长度
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            #用当前位置覆盖字典中的位置
            res = max(res, tmp)
        return res

if __name__ == '__main__':
    # do test
    testDemo = Solution()
    print "abcabcbb:",testDemo.lengthOfLongestSubstring("abcabcbb")
    print "bbbbb:", testDemo.lengthOfLongestSubstring("bbbbb")
    print "pwwkew:", testDemo.lengthOfLongestSubstring("pwwkew")