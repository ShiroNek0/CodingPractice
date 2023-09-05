public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        var left = 0;
        var right = 0;
        var result = 0;
        var dict = new Dictionary<char, int>();

        if (String.IsNullOrEmpty(s))
        {
            return 0;
        }

        for (; right < s.Length; right++)
        {
            //
            if (dict.ContainsKey(s[right]))
            {
                left = Math.Max(dict[s[right]] + 1, left);
                dict.Remove(s[right]);
            }

            dict.Add(s[right], right);

            result = Math.Max(result, right - left + 1);
        }

        return result;
    }
}




// Dumber solution, but have better stats on Leetcode?
// public class Solution {
//     public int LengthOfLongestSubstring(string s) {
//         var firstIndex = 0;
//         var secondIndex = 0;
//         var result = 1;

//         if (String.IsNullOrEmpty(s)) 
//         {
//             return 0;
//         }

//         for (int i = 1; i < s.Length; i++)
//         {
//             for (int j = firstIndex; j < i; j++)
//             {
//                 if (s[j] == s[i])
//                 {
//                     firstIndex = j+1;
//                     break;
//                 }
//             }

//             result = Math.Max(result, i - firstIndex + 1);
//         }

//         return result;
//     }
// }