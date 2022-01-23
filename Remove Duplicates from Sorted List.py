# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        node =head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        lengths=len(nodes)
        i=0

        while i<(lengths-1):
            if(nodes[i]==nodes[i+1]):
                nodes.remove(nodes[i])
                lengths=lengths-1
                i=i-1
            i=i+1
        head=None
        for i in nodes:
            if(head==None):
                my=ListNode(i)
                head=my
                sec=head
            else:
                new=ListNode(i)
                sec.next=new
                sec=sec.next
        return head