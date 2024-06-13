// See https://aka.ms/new-console-template for more information

using DefaultNamespace;

Console.WriteLine("Hello, World!");

// RotateArray rotateArray = new RotateArray();
// int[] nums = {1, 2, 3, 4, 5};
// int k = 2;
// rotateArray.Rotate(nums, k);
//
// rotateArray.Rotate([-1,-100,3,99],2);

// ValidPalindrome p = new ValidPalindrome();
// Console.WriteLine(p.IsPalindrome("A man, a plan, a canal: Panama"));

// ListNode head = new ListNode(1);
// head.next = new ListNode(2);
// head.next.next = new ListNode(3);
// head.next.next.next = new ListNode(4);
// head.next.next.next.next = new ListNode(5);
//
// ListNode.LinkedListProblems solution = new ListNode.LinkedListProblems();
// solution.ReverseList(head);

TreeNode node4 = new TreeNode(4);
TreeNode node5 = new TreeNode(5);
TreeNode node2 = new TreeNode(2, node4, node5);
TreeNode node3 = new TreeNode(3);
TreeNode root = new TreeNode(1, node2, node3);

BinaryTreeProblems problems = new BinaryTreeProblems();
int maxDepth = problems.MaxDepth(root);
Console.WriteLine(maxDepth);  // Outputs: 3