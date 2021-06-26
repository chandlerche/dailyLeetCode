public class Solution {
        private int Fun(int[] nums1, int[] nums2)
        {
            int v = 0;
            Dictionary<long,int> dic = new Dictionary<long, int>();
            foreach (var num1 in nums1)
            {
                long p = (long)num1 * num1;
                dic[p] = dic.TryGetValue(p, out var n) ? n+ 1 : 1;
            }

            for (int i = 0; i < nums2.Length; i++)
            {
                for (int j = i+1; j < nums2.Length; j++)
                {
                    if (dic.TryGetValue((long)nums2[i] * nums2[j], out var n))
                    {
                        v += n;
                    }
                }
            }
            return v;
        }
        public int NumTriplets(int[] nums1, int[] nums2)
        {
            return Fun(nums1,nums2) + Fun(nums2,nums1);
        }
}