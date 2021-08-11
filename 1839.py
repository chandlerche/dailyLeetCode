class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        next_vowel = {"a": {"a", "e"},          # 找到各个元音字母下一个合法的元音字母应该是哪个
                      "e": {"e", "i"},
                      "i": {"i", "o"},
                      "o": {"o", "u"},
                      "u": {"u"},
                      }
        left = res = 0                          # 初始化左指针和结果变量
        while left < len(word) - 4:             #
            if word[left] == "a":               # 一旦检测到字母“a”则开始探索
                right = left                    # 定义右指针，开始向右寻找，直到遇到非法字符
                while right + 1 < len(word) and word[right+1] in next_vowel[word[right]]:
                    right += 1
                if word[right] == "u":          # 整个aeiou子串找全了
                    res = max(res, right - left + 1)
                left = right                    # 更新左指针
            left += 1                           # 左指针右移
        return res