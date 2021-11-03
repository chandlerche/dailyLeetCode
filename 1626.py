class Solution:
    def bestTeamScore(self, scores, ages):
        score_age = list(zip(scores, ages))
        score_age = sorted(score_age, key = lambda x : (x[1], x[0]))
        dp = [0] * len(score_age)
        dp[0] = score_age[0][0]    # 必有一个元素

        for i in range(1, len(score_age)):
            # if score_age[i][1] == score_age[i - 1][1]:
            #     dp[i] = dp[i - 1] + score_age[i][0]

            # else:
            max_front = 0
            for j in range(i):
                if score_age[j][0] <= score_age[i][0] and dp[j] > max_front:    # 年龄比其小的里面只能选择分数小的
                    max_front = dp[j]

            dp[i] = max_front + score_age[i][0]

        return max(dp)