class MyCalendarThree:
    def __init__(self):
        self.lazy = collections.defaultdict(int)
        self.tree = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        def update(s, e, l=0, r=10 ** 9, id=0):  # 左闭右开
            if r <= s or e <= l:
                return
            if s <= l < r <= e:  # 范围符合要求，直接更新tree和懒惰树相应节点的值
                self.lazy[id] += 1  # 懒惰树节点值储存未向下层传递的tree值
                self.tree[id] += 1
            else:  # 范围比较小，先向下更新tree和懒惰树
                mid = (l + r) // 2
                update(s, e, l, mid, 2 * id + 1)
                update(s, e, mid, r, 2 * id + 2)
                self.tree[id] = self.lazy[id] + max(self.tree[2 * id + 1], self.tree[2 * id + 2])  # tree的节点值为之前存的懒惰树节点值+下层先上层传递的tree值。

        update(start, end)
        return self.tree[0] #返回tree的root节点的值