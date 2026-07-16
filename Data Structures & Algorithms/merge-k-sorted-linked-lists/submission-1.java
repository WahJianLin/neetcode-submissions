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
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode ret = null;
        for(int i = 0; i < lists.length; i++){
            if(lists[i]!=null){
                if(ret==null){
                    ret = lists[i];
                } else {
                    ret = mergeTwo(ret, lists[i]);
                }
            }
        }
        return ret;
    }

    private ListNode mergeTwo(ListNode a, ListNode b){
        ListNode ret = new ListNode();
        ListNode current = ret;
        while(a!=null && b!=null){
            if(a.val<=b.val){
                current.next = a;
                a=a.next;
            } else {
                current.next = b;
                b=b.next;
            }
            current = current.next;
        }
        if(a==null){
            current.next = b;
        }else {
            current.next = a;
        }
        return ret.next;
    }
}
