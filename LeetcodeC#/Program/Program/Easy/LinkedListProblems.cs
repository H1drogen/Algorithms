namespace DefaultNamespace;
using System.Collections.Generic;

public class ListNode { 
    public int val;
    public ListNode next; 
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
    
public class LinkedListProblems
{
        public void DeleteNode(ListNode node) {
            node.val = node.next.val;
            node.next = node.next.next;
        }
        // node = node.next does not work because In C#, parameters are passed by value
        // This means that when you pass a ListNode object to the DeleteNode method, a copy of the reference to the object is created
        //  if you change the copy of the reference itself to point to a different object (like node = node.next), this change will not be visible outside the method
        
        // When you modify the properties of the object that the reference points to (like node.val = node.next.val), those changes will be visible outside the method because both the original reference and the copy point to the same object.

        public ListNode RemoveNthFromEnd(ListNode head, int n)
        {
            int length = 0;
            ListNode current = head;
            while (current.next != null)
            {
                length += 1;
                current = current.next;
            }

            if (length + 1 == n)
            {
                return head.next;
            }

            current = head;
            for (int i = 0; i < length - n; i++)
            {
                current = current.next;
            }

            current.next = current.next.next;
            return head;
        }
        // use a 2 pointer approach, with one pointer (int n) steps ahead of the other
        
        public ListNode ReverseList(ListNode head) {
            if (head == null) 
            {
                return head;
            }
            ListNode reversed = new ListNode(head.val);
            head = head.next;
            while (head != null) 
            {
                ListNode entry = new ListNode(head.val);
                entry.next = reversed;
                reversed = entry;
                head = head.next;
            }
            return reversed;
        }

        public ListNode refined_answer(ListNode head)
        {
            ListNode prev = null;
            ListNode current = head;
            while (current != null) {
                ListNode next = current.next;
                current.next = prev;
                prev = current;
                current = next;
            }
            return prev;
        }
    }
}