package leetcode.easy;

import Interfaces.TreeNode;

public class maximum_depth_tree {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        maxDepth(root.left);

    }
}
