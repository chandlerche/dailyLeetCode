class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, l = 0, len(formula)
        atom = ''
        count = 0
        stack = [{}]
        while i < l:
            c = formula[i]
            if 'A' <= c <= 'Z':
                atom, i = self.getAtom(formula, l, i)
                if i < l and '0' <= formula[i] <= '9':
                    count, i = self.getCount(formula, l, i)
                    stack[-1][atom] = stack[-1].get(atom, 0) + count
                else:
                    stack[-1][atom] = stack[-1].get(atom, 0) + 1
            elif c == '(':
                stack.append({})
                i += 1
            else:
                i+=1
                if i < l and '0' <= formula[i] <= '9':
                    count, i = self.getCount(formula, l, i)
                else:
                    count = 1
                counter = stack.pop()
                for k in counter:
                    counter[k] *= count
                self.mergeCounter(stack[-1], counter)
        return self.formatCounter(stack[-1])
    def formatCounter(self, counter):
        keys = sorted(counter.keys())
        ret = ''
        for key in keys:
            ret += key
            if counter[key] > 1:
                ret += str(counter[key])
        return ret
        
    def mergeCounter(self, counter1, counter2):
        merged_counter = {}
        for k in counter2:
            counter1[k] = counter1.get(k, 0) + counter2[k]
                
    def getAtom(self, formula, l, i):
        s = formula[i]
        i+=1
        while i < l:
            if 'a' <= formula[i] <= 'z':
                s += formula[i]
            else:
                break
            i+=1
        return s, i

    def getCount(self, formula, l, i):
        cnt = int(formula[i])
        i+=1
        while i < l:
            if '0' <= formula[i] <= '9':
                cnt = cnt * 10 + int(formula[i])
            else:
                break
            i+=1
        return cnt, i