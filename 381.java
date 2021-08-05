class RandomizedCollection {
    private List<Integer> nums;//存储 val 元素
    private Map<Integer, Set<Integer>> map;//存储每个 val 的下标集合
    public RandomizedCollection() {
        nums = new ArrayList();
        map = new HashMap();
    }
    
    public boolean insert(int val) {
        nums.add(val);//元素列表直接添加到末尾，O(1)
        Set<Integer> set = map.getOrDefault(val, new HashSet<Integer>());
        set.add(nums.size() - 1);//set里加入下标，O(1)
        map.put(val, set);
        return set.size() == 1;//返回是否重复，即set里存了多少个 val 对应的下标，O(1)
    }

    public boolean remove(int val) {
        if(!map.containsKey(val))return false;
        //获取一个 val 值对应的下标，hash操作，为O(1)
        Iterator<Integer> it = map.get(val).iterator();
        int i = it.next();
        //获取列表尾部元素，并换到 val 的位置
        int lastNum = nums.get(nums.size() - 1);
        nums.set(i, lastNum);
        //删除 val 的位置，尾部元素的位置
        map.get(val).remove(i);
        map.get(lastNum).remove(nums.size() - 1);
        //更新尾部元素的下标集合
        if(i < nums.size() - 1)map.get(lastNum).add(i);
        if(map.get(val).size() == 0)map.remove(val);//如果val只出现一次，直接删除他的下标集合
        nums.remove(nums.size() - 1);
        return true;
    }
    
    public int getRandom() {
        return nums.get((int)(Math.random() * nums.size()));
    }
}