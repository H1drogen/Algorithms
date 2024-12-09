import Interfaces.TreeNode;
import leetcode.easy.maximum_depth_tree;

import java.util.HashMap;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        // Press Alt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it.
        // Create the tree [3,9,20,null,null,15,7]
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        // Create an instance of maximum_depth_tree
        maximum_depth_tree tree = new maximum_depth_tree();

        // Call the maxDepth method and print the result
        int depth = tree.maxDepth(root);
        System.out.println("Maximum depth of the tree: " + depth);

    }
}