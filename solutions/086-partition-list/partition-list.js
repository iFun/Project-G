// Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
//
// You should preserve the original relative order of the nodes in each of the two partitions.
//
// Example:
//
//
// Input: head = 1->4->3->2->5->2, x = 3
// Output: 1->2->2->4->3->5
//
//


/*
 * @lc app=leetcode id=86 lang=javascript
 *
 * [86] Partition List
 *
 * https://leetcode.com/problems/partition-list/description/
 *
 * algorithms
 * Medium (37.42%)
 * Likes:    672
 * Dislikes: 184
 * Total Accepted:    165.9K
 * Total Submissions: 443.3K
 * Testcase Example:  '[1,4,3,2,5,2]\n3'
 *
 * Given a linked list and a value x, partition it such that all nodes less
 * than x come before nodes greater than or equal to x.
 * 
 * You should preserve the original relative order of the nodes in each of the
 * two partitions.
 * 
 * Example:
 * 
 * 
 * Input: head = 1->4->3->2->5->2, x = 3
 * Output: 1->2->2->4->3->5
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    if (!head || !head.next) return head;
    const dummySmall = new ListNode();
    const dummyLarge = new ListNode();

    let small = dummySmall;
    let large = dummyLarge;
    let current = head;

    while(current){
        if(current.val < x){
            small.next = current;
            small = small.next
        }else{
            large.next = current;
            large = large.next
        }
        current = current.next;
    }
    
    small.next = dummyLarge.next;
    large.next = null;
    return dummySmall.next;
    
};


