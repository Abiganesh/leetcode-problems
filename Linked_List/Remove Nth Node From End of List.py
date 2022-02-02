# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node =head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        lengths=len(nodes)
        if(lengths==1):
            return None
        else:
            pos=lengths-n-1
            if(pos<0):
                node=head
                head=node.next
                return head
            else:
                node=head
                while(pos!=0):
                    node=node.next
                    pos=pos-1
                node.next=node.next.next
                return head

