/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        // Run 2 pointer for 2 ListNode
        // Compare next element between 2 pointer
        // Linked current node to smaller pointer
        // Loop until one pointer run is done, then concat to remaining list of remain pointer
        if (list1 == null)
        {
            return list2;
        }
        else if (list2 == null)
        {
            return list1;
        }
        
        var currNode = new ListNode();

        if (list1.val <= list2.val)
        {
            currNode = list1;
            list1 = list1.next;
        }
        else
        {
            currNode = list2;
            list2 = list2.next;
        }

        var startNode = currNode;

        while(list1 != null && list2 != null)
        {
            if (list1.val <= list2.val)
            {
                currNode.next = list1;
                list1 = list1.next;
            }
            else 
            {
                currNode.next = list2;
                list2 = list2.next;
            }

            currNode = currNode.next;
        }

        if (list1 == null)
        {
            currNode.next = list2;
        }
        else 
        {
            currNode.next = list1;
        }

        return startNode;
    }
}