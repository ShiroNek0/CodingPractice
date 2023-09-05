public class Solution {
    public bool IsAnagram(string s, string t) 
    {
        char[] sCharacters = s.ToArray();
        Array.Sort(sCharacters);
        string sSorted = new string(sCharacters);

        char[] tCharacters = t.ToArray();
        Array.Sort(tCharacters);
        string tSorted = new string(tCharacters);

        return sSorted == tSorted;
    }
}