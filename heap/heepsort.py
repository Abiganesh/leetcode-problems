import heapq
minHeap = [3,1,25,4]
ascending=[]
heapq.heapify(minHeap)
length=len(minHeap)
while(length!=0):
    pop=heapq.heappop(minHeap)
    ascending.append(pop)
    length=length-1
print(ascending)
    
