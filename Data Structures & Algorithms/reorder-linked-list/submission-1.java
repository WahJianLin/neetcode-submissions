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

/*
get N first 
*/
class Solution {
    public void reorderList(ListNode head) {
        if(head.next!=null){
            ListNode slow = head;
            ListNode fast = head.next;
            while(fast!=null && fast.next!=null){
                slow=slow.next;
                fast=fast.next.next;
            }
            ListNode holder = slow.next;
            ListNode previous = null;
            slow.next=null;
            slow=holder.next;
            holder.next=null;
            while(slow!=null){
                previous = slow;
                slow=slow.next;
                previous.next=holder;
                holder=previous;
            }

            boolean flip = true;
            ListNode original = head;
            ListNode standard = head.next;
            while(standard!=null || holder!=null){
                if(flip){
                    original.next = holder;
                    holder=holder.next;
                }else{
                    original.next = standard;
                    standard=standard.next;
                }
                original=original.next;
                flip=!flip;
            }
        }
    }
}
