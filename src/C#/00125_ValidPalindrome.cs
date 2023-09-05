public class Solution {
    public bool IsPalindrome(string s) 
    {
        // Double pointer
        // Pointer left run from (middle=> 0)
        // Pointer right run from (middle => end)
        // Check each character 
        // Return true if all match, false otherwise
        var input = GetAlphanumericString(s).ToLower();
        int leftPt = 0;
        int rightPt = 0;

        if (input.Length % 2 == 0)
        {
            leftPt = input.Length/2 - 1;
            rightPt = leftPt + 1;
        }
        else
        {
            leftPt = input.Length/2 - 1;
            rightPt = leftPt + 2;
        }

        for (; rightPt < input.Length; rightPt++)
        {
            if (input[rightPt] != input[leftPt])
            {
                return false;
            }

            leftPt--;
        }

        return true;
    }

    private string GetAlphanumericString(string input)
    {
        return new String(input.Where(x => char.IsLetterOrDigit(x)).ToArray());
    }
}