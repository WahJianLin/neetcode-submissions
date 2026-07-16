/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

/*
    Same algorithm as before except we only record the last val
*/
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if(root == null){
            return ret;
        }
        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);
        
        while(!que.isEmpty()){
            int size = que.size();
            while(size>0){
                TreeNode target = que.remove();
                if(size==1){
                    ret.add(target.val);
                }
                if(target.left!=null){
                    que.add(target.left);
                }
                if(target.right!=null){
                    que.add(target.right);
                }
                size --;
            }
        }
        
        return ret;
    }
}
