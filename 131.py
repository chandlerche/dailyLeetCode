class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        point_array = [[] for i in range(length)]

        for j in range(length):
            for i in range(length - j):
                if self.is_palindrome_in_string(s, i, j):
                    point_array[j].append(length - i)

        path_array = [[] for i in range(length)]

        for i in range(length - 1, -1, -1):
            for point_index in point_array[i]:
                now_path = s[i:point_index]
                if point_index == length:
                    path_array[i].append([now_path])
                else:
                    for path_list in path_array[point_index]:
                        a = path_list.copy()
                        a.append(now_path)
                        path_array[i].append(a)

        for result_list in path_array[0]:
            result_list.reverse()

        return path_array[0]

    def is_palindrome_in_string(self, s, start_x, start_y) -> bool:
        y = start_y
        for i in range(len(s) - start_x - start_y):
            if s[y + i] != s[len(s) - start_x - i - 1]:
                return False
            elif y + i >= len(s) - start_x - i - 1:
                return True
        return True