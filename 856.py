class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        s = ''
        for i in range(len(S)-1):
            if S[i] == '(':
                if S[i+1] == "(": 
                    s += "("
                else:
                    s += '1'
            else:
                if S[i+1] == '(':
                    s += '+'
                else:
                    s += ')*2'
        return eval(s)