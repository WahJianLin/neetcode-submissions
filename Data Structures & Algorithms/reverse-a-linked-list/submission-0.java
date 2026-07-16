/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next==null){
            return head;
        }
        ListNode chain = null;
        ListNode current = head;

        while(current.next!=null){
            ListNode previous = current;
            current = current.next;
            if(chain == null){
                previous.next=null;
                chain = previous;
            } else {
                previous.next = chain;
                chain=previous;
            }
        }
        current.next = chain;
        return current;
    }
}
