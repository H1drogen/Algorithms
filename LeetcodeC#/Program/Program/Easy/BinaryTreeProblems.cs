using System.Net;
using System.Xml.Xsl;

namespace DefaultNamespace;

public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class BinaryTreeProblems
{
    public int MaxDepth(TreeNode root)
    {
        int count = 2;
        if (root.right != null)
        {
            RightSide(root.right, count);
        }

        if (root.left != null)
        {
            LeftSide(root.left, count);
        }

        
        void LeftSide(TreeNode leftroot, int leftcount)
        {
            if (leftroot.left != null)
            {
                int number = leftcount + 1;
                LeftSide(leftroot.left, number);
            }
            else
            {
                if (leftcount > count)
                {
                    count = leftcount;
                }
            }

            if (leftroot.right != null)
            {
                int number = leftcount + 1;
                RightSide(leftroot.right, number);
            }
            else
            {
                if (leftcount > count)
                {
                    count = leftcount;
                }
            }
        }

        void RightSide(TreeNode rightroot, int rightcount)
        {
            if (rightroot.left != null)
            {
                int number = rightcount + 1;
                LeftSide(rightroot.left, number);
            }
            else
            {
                if (rightcount > count)
                {
                    count = rightcount;
                }
            }

            if (rightroot.right != null)
            {
                int number = rightcount + 1;
                RightSide(rightroot.right, number);
            }
            else
            {
                if (rightcount > count)
                {
                    count = rightcount;
                }
            }
        }

        return count;
    }
    
    public bool IsSymmetric(TreeNode root) {
        bool check(TreeNode leftroot, TreeNode rightroot)
        {
            if (leftroot.left == rightroot.right && leftroot.right == rightroot.left)
            {
                check(leftroot.left, rightroot.right);
                check(leftroot.right, rightroot.left);
                return true;
            }
            else
            {
                return false;
            }
        }

        return check(root.left, root.right);
    }
}