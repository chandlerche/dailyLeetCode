class Solution(object):
    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        modnum = 10**9 + 7;
        currentList = [1];
        newList = [];
        current = 1;
        while (current < n):
            current += 1;
            before = 0;
            start = max(0, k - n + current - 2);
            if (start > 0):
                before = currentList[start - 1];
            for i in range(start, len(currentList)):
                count = currentList[i];
                value = (count * (current - 1) + before);
                if (value >= modnum):
                    value %= modnum;
                currentList[i] = value;
                before = count;
            #print(i, k)
            if (len(currentList) < k):
                currentList.append(before);
            #print currentList;
        return currentList[k-1];