class Node:
    def __init__(self,value=None):
        self.value=value
        self.Next=None
        
class MyLinkedList(object):
    def __init__(self):
        self.head=None 
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.Next
        return (str(nodes))
    def addAtHead(self, value):
        if(self.head==None):   
            my=Node(value)
            self.head=my
        else:
            new=Node(value)
            new.Next=self.head
            self.head=new
    def addAtTail(self, value):
        if(self.head==None):   
            my=Node(value)
            self.head=my
        else:
            sec=self.head
            while(sec.Next!=None):

                sec=sec.Next
            last=Node(value)
            sec.Next=last
    def addAtIndex(self, index, value):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.Next
       
        length=len(nodes)
        
        if(index==0):
            if(length==0):
                my=Node(value)
                self.head=my
            elif(length>0):
                mid=Node(value)
                mid.Next=self.head
                self.head=mid
        elif(length<index):
            return -1
        else:
            pos=index
            sec=self.head
            while(pos!=1):
                pos=pos-1
                sec=sec.Next
            mid=Node(value)
            mid.Next=sec.Next
            sec.Next=mid
    def deleteAtIndex(self, index):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.Next
       
        length=len(nodes)
       
        if(index==0):
            if(length==1):
                self.head=None
            elif(length>1):
                nen=self.head
                self.head=nen.Next
        elif(index>=length):
            return -1
        else:
            pos=index
            sec=self.head
            while(pos!=1):
                pos=pos-1
                sec=sec.Next
            sec.Next=sec.Next.Next
        
    def get(self, index):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.Next
       
        length=len(nodes)
        if(index==length):
            return -1
        elif(index==0):
            return self.head.value
        elif(index>=length):
            return -1
        else:
            pos=index
            sec=self.head
            while(pos!=1):
                pos=pos-1
                sec=sec.Next
            return sec.Next.value