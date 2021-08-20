#import re
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # length=re.search("",s)
        own=[]
        done=[]
        c=0
        count=0
        if(len(s)==0):
            return 0
        elif(len(s)==1):
            return 1
        else:
            for i,j in zip(s,range(0,len(s))):
                if i in done:
                    if j==len(s)-1:
                        own.append(count)
                        count=0
                        m=0
                        a=1
                        while (a!=0):
                            if(done[m]==i):
                                done.remove(done[m])
                                c=len(done)
                                break
                            else:
                                done.remove(done[m])
                        done.append(i)
                        count=count+1
                        own.append(count)
                    else:
                        own.append(count)
                        count=0
                        m=0
                        a=1
                        while (a!=0):
                            if(done[m]==i):
                                done.remove(done[m])
                                c=len(done)
                                break
                            else:
                                done.remove(done[m])
                        done.append(i)
                        count=count+1+c
                else:
                    if j==len(s)-1:
                        
                        count=count+1
                        own.append(count)
                        done.append(i)
                    else:
                        done.append(i)
                        count=count+1


            final = sorted(own)
            final=list(final)
            return final[len(final)-1]