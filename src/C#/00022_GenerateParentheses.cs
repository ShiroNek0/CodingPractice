public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        Generate(0, 0, "", n, result);
        return result;
    }

    public void Generate(int open, int close, string input, int n, IList<string> result)
    {
        if (input.Length == n*2) 
        {
            result.Add(input);
        }

        if (open < n) 
        {
            Generate(open+1, close, input + "(", n, result);
        }

        if (close < open)
        {
            Generate(open, close+1, input + ")", n, result);
        }
    }
}