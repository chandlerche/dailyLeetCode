class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if len(word) == 0:
            return [""]

        dp = [[]] * (len(word) - 1)
        dp.append(["1", word[-1]])

        for idx in range(len(word) - 2, -1, -1):
            suffixes = set()
            for l in range(1, len(word) - idx):
                for suffix in dp[idx + l]:
                    suffixes.add(word[idx:idx+l] + suffix)
                    if suffix[0].isalpha():
                        suffixes.add(str(l) + suffix)

            suffixes.add(str(len(word) - idx))
            dp[idx] = list(suffixes)

        return dp[0]