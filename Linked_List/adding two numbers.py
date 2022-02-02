# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        one=l1
       
        ons=""
        while(one.next!=None):
            
            ons=ons+str(one.val)
            one=one.next
        ons=ons+str(one.val)
        onos=ons[::-1]
        print(onos)
        
        two=l2
        tos=""
        while(two.next!=None):
            
            tos=tos+str(two.val)
            two=two.next
        tos=tos+str(two.val)
        toos=tos[::-1]
        
       
        rev=long(onos)+long(toos)
        rev12=str(rev)
        
        revs=rev12[::-1]
        
        
      
        head=None
        print(revs)
        for i in revs:
            if(head==None):
                my=ListNode(i)
                head=my
                sec=head
            else:
                new=ListNode(i)
                sec.next=new
                sec=sec.next
        return head
        
            
       
        
        