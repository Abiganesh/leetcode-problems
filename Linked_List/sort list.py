# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node =head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        lengths=len(nodes)
        sortedlist=sorted(nodes)
        head=None
        for i in sortedlist:
            if(head==None):
                my=ListNode(i)
                head=my
                sec=head
            else:
                new=ListNode(i)
                sec.next=new
                sec=sec.next
        return head
       