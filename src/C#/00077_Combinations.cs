public class Solution {
    private IList<IList<int>> res = new List<IList<int>>();

    public IList<IList<int>> Combine(int n, int k) {
        // Backtracking
        // Generate the correct combination by Backtracking
        // [1, 2, 3, 4, 5]
        // list.Add(1)
        // backtrack([2->5], list)
        // list.remove (1)
        var initList = new List<int>();
        Backtrack(1, n, k, initList);
        return res;
    }

    private void Backtrack(int start, int end, int k, List<int> currList)
    {
        if (currList.Count == k)
        {
            res.Add(new List<int>(currList));
            return;
        }

        for (int i = start; i <= end; i++)
        {
            currList.Add(i);
            Backtrack(i+1, end, k, currList);
            currList.RemoveAt(currList.Count - 1);
        }
    }
}