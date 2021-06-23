class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {

    ArrayList<int[]> list = new ArrayList<>();
    int i=0;
    int j=0;
    while (i<firstList.length&&j<secondList.length){
        int a1=firstList[i][0];
        int a2=firstList[i][1];
        int b1=secondList[j][0];
        int b2=secondList[j][1];
        if(b2>a2){
            i++;
        }else {
            j++;
        }
        if(b2>=a1&&a2>=b1){
            int left=Math.max(a1,b1);
            int right =Math.min(a2,b2);
            list.add(new int[]{left,right});
        }
    }
    return list.toArray(new int[list.size()][]);
    }
}