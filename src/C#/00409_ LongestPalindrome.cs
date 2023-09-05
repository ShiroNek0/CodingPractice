public class Solution
{
    public int LongestPalindrome(string s)
    {
        // aaa bbb ccc aaa
        // Do the character count
        // Counting all character that has even count +  each(character odd count - 1) (except 1 odd count char that has middle)
        /// aaa cddc aaa

        var dict = new Dictionary<char, int>();

        int temp;
        bool isExist;
        foreach (char c in s)
        {
            isExist = dict.TryGetValue(c, out temp);
            if (isExist)
            {
                dict[c] += 1;
            }
            else
            {
                dict.Add(c, 1);
            }
        }

        var evenCount = 0;
        var maxOddCount = 0;
        var total = 0;

        foreach (KeyValuePair<char, int> entry in dict)
        {
            if (entry.Value % 2 == 0)
            {
                evenCount += entry.Value;
            }
            else
            {
                maxOddCount =  maxOddCount == 0 ? entry.Value : maxOddCount + entry.Value - 1;
            }

            total += entry.Value;
        }

        return evenCount + maxOddCount;
    }
}