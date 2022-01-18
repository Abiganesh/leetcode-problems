"""nums = [-2,0,1,1,2]
final=[]
z=0
last=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(i+j+1,len(nums)):
            total=nums[i]+nums[j]+nums[k]
            if(total==0):
                final.append([nums[i],nums[j],nums[k]])
print(final)
print(len(final))
if(len(final)>1):
    for m in range(0,len(final)):
        for n in range(m+1,len(final)):
            print(final[m])
            print(final[n])
            if(set(final[m])!=set(final[n])):
                
                last.append(final[m])
    if(len(last)==0):
        last.append(final[0])
    print(last)
else:
    print(final)
    """
nums = [3,0,-2,-1,1,2]
final=[]
z=0
last=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(i+j+1,len(nums)):
            print("i",i)
            print("j",j)
            print("k",k)
            total=nums[i]+nums[j]+nums[k]
            if(total==0):
                 print("ini",i)
                 print("inj",j)
                 print("ink",k)
                 final.append([nums[i],nums[j],nums[k]])
print(final)
print(len(final))
if(len(final)>1):

    for m in range(0,len(final)):
        o=0
        for n in range(0,m):
            print("n",n)
            print("m",m)
            
          
            if(set(final[m])==set(final[n])):
                o=1
                break
        if(o==0):
            last.append(final[m])
    if(len(last)==0):
        last.append(final[0])
    print(last)
else:
    print(final)
