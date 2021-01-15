class Solution {
	public boolean canReach(int[] arr, int start) {
		return dfs(arr, start);
	}

	private boolean dfs(int[] arr, int st) {
		if (st < 0 || st >= arr.length || arr[st] == -1)
			return false;
		int step = arr[st];
		arr[st] = -1;
		return step == 0 || dfs(arr, st + step) || dfs(arr, st - step);
	}
}