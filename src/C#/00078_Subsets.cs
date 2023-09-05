public class Solution {
    public IList<IList<int>> Subsets(int[] nums) 
    {
        // Backtrack
        // Loop nums
        // Add the i element of nums
        // Do backtrack with nums[i+1, n]
        // remove i element
        IList<IList<int>> result = new List<IList<int>>();
        var currList = new List<int>();
        Backtrack(nums, 0, nums.Length - 1, currList, result);
        return result;
    }

    private void Backtrack(int[] nums, int start, int end, IList<int> currList, IList<IList<int>> result)
    {
        result.Add(new List<int>(currList));

        for (int i = start; i <= end; i++)
        {
            currList.Add(nums[i]);
            Backtrack(nums, i+1, end, currList, result);
            currList.RemoveAt(currList.Count - 1);
        }
    }
}