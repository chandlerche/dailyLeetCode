from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        num_students, num_mentors = len(students), len(mentors)

        def cal(ans1, ans2):
            return [a1 == a2 for a1, a2 in zip(ans1, ans2)].count(True)
        dist = [[0 for _ in range(num_mentors)] for _ in range(num_students)]
        for i1, student in enumerate(students):
            for i2, mentor in enumerate(mentors):
                dist[i1][i2] = cal(student, mentor)

        self.ans = 0

        def backtrack(rest_students: set, rest_mentors: set, ans_cur):

            if not rest_students and not rest_mentors:
                self.ans = max(self.ans, ans_cur)
                return
            student_id = rest_students.pop()
            for mentor_id in rest_mentors:
                rest_mentors.remove(mentor_id)
                backtrack(rest_students, rest_mentors, ans_cur+dist[student_id][mentor_id])
                rest_mentors.add(mentor_id)
            rest_students.add(student_id)

        backtrack(set(range(num_students)), set(range(num_mentors)), 0)
        return self.ans