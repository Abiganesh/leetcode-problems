def reverse(x):
        y=x
        rev = 0
        p1=2147483647
        p2=-2147483648
        if(y>p1):
            return 0
        elif(y<p2):
            return 0
        if(y<0):
            out='-'
            y=str(y)
            y=y[1:]
            y=int(y)
        else:
            out=""
        while(y > 0):
            a = y % 10
            rev = rev * 10 + a
            y = y // 10
        if(rev>p1):
            return 0
        elif(rev<p2):
            return 0
        return out+str(rev)
x=int(input())
print(reverse(x))
