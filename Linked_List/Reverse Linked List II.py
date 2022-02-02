# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        node =head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        if(len(nodes)==1):
            return head

            
        else:
            #leftindex=nodes.index(left)
            #rightindex=nodes.index(right)
            print(left-1)
            print(right)
            parnodes=nodes[left-1:right]
            print(parnodes)
            parnodes.reverse()
            nodes[left-1:right]=parnodes
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

