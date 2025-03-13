# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0
        countB = 0
        tempA = headA
        tempB = headB
        while tempA:
            countA += 1
            tempA = tempA.next
        while tempB:
            countB += 1
            tempB = tempB.next
        if countA > countB:
            for i in range(countA - countB):
                headA = headA.next
        else:
            for i in range(countB - countA):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
