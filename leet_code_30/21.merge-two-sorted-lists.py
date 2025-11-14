#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        We will create a dummy node to act as the head of the merged list.
        We will also maintain a tail pointer to keep track of the last node in the merged list.
        We will iterate through both lists until we reach the end of one of them.
        At each step, we will compare the values of the current nodes of both lists.
        We will append the smaller value node to the merged list and move the corresponding pointer forward.
        After the loop, if there are remaining nodes in either list, we will append them to the merged list.
        Finally, we will return the next node of the dummy node, which is the head of the merged list.
        Tracing:
        list1: 1 -> 3 -> 5
        list2: 2 -> 4 -> 6
        dummy -> None
        tail -> dummy
        Compare 1 and 2: 1 < 2, append 1 to merged list
        dummy -> 1
        tail -> 1
        Compare 3 and 2: 2 < 3, append 2 to merged list
        dummy -> 1 -> 2
        tail -> 2
        Compare 3 and 4: 3 < 4, append 3 to merged list
        dummy -> 1 -> 2 -> 3
        tail -> 3
        Compare 5 and 4: 4 < 5, append 4 to merged list
        dummy -> 1 -> 2 -> 3 -> 4
        tail -> 4
        Compare 5 and 6: 5 < 6, append 5 to merged list
        dummy -> 1 -> 2 -> 3 -> 4 -> 5
        tail -> 5
        list1 is exhausted, append remaining nodes from list2
        dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        return dummy.next -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        '''
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
# @lc code=end

