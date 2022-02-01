import heapq
maxHeap = [3,1,25,4]
maxHeap = [-x for x in maxHeap]
descending=[]
heapq.heapify(maxHeap)
length=len(maxHeap)
while(length!=0):
    pop=heapq.heappop(maxHeap)
    descending.append(pop*-1)
    length=length-1
print(descending)
    
