# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None: return None
        if l1 == None: return ListNode(l2.val, self.addTwoNumbers(None, l2.next))
        if l2 == None: return ListNode(l1.val, self.addTwoNumbers(None, l1.next))
        result = l1.val+l2.val
        if l1.next == None:
            return ListNode(result, self.addTwoNumbers(None, l2.next)) if result<10 else \
                   ListNode(result-10, self.addTwoNumbers(ListNode(1), l2.next))
        if l2.next == None:
            return ListNode(result, self.addTwoNumbers(None, l1.next)) if result<10 else \
                   ListNode(result-10, self.addTwoNumbers(ListNode(1), l1.next))
        return ListNode(result, self.addTwoNumbers(l1.next, l2.next)) if result<10 else \
               ListNode(result-10, self.addTwoNumbers(self.addTwoNumbers(l1.next, ListNode(1)), l2.next))
        
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1,l2).val)
print(Solution().addTwoNumbers(l1,l2).next.val)
print(Solution().addTwoNumbers(l1,l2).next.next.val)
