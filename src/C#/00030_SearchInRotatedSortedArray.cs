public class Solution
{
    public int Search(int[] nums, int target)
    {
        // find the pivot point (must be log N)
        // search number is correspond range (nums[k] -> nums[n-1]) (nums[0] -> nums[k-1])
        // search by binary search (logN)

        if (nums.Length == 0)
        {
            return -1;
        }

        if (nums.Length == 1)
        {
            return nums[0] == target ? 0 : -1;
        }

        var pivotIndex = GetPivotPointIndex(nums, 0, nums.Length - 1);
        if (pivotIndex != 0)
        {
            if (nums[nums.Length - 1] < target)
            {
                return BinarySearch(nums, 0, pivotIndex - 1, target);
            }
            else
            {
                return BinarySearch(nums, pivotIndex, nums.Length - 1, target);
            }
        }
        else
        {
            return BinarySearch(nums, 0, nums.Length - 1, target);
        }
    }

    public int GetPivotPointIndex(int[] nums, int start, int end)
    {
        int middle = (start + end) / 2;
        if (nums[start] <= nums[middle] && nums[middle] <= nums[end])
        {
            return start;
        }

        if (nums[start] > nums[middle])
        {
            return GetPivotPointIndex(nums, start, middle);
        }

        if (nums[middle] > nums[end])
        {
            return GetPivotPointIndex(nums, middle+1, end);
        }

        return 0;
    }

    public int BinarySearch(int[] nums, int start, int end, int target)
    {
        int middle = (start + end) / 2;

        if (middle == start && middle == end)
        {
            if (nums[middle] == target)
            {
                return middle;
            }
            else
            {
                return -1;
            }
        }

        if (nums[middle] >= target)
        {
            return BinarySearch(nums, start, middle, target);
        }
        else
        {
            return BinarySearch(nums, middle+1, end, target);
        }
    }
}