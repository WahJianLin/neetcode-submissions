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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode current = head;
        int count = 0;
        while(current!=null){
            current = current.next;
            count++;
        }
        if(count == 1){
            return null;
        }
        if(count == n){
            return head.next;

        }
        int result = count - n -1;
        current = head;
        while(result>0){
            current = current.next;
            result --;
        }
        current.next = current.next.next;
        return head;
    }
}
