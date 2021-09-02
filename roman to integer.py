
Roman = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
rom="IX"
p = 0
ans = 0
n = len(rom)

for i in range(n-1, -1, -1):
    if Roman[rom[i]] >= p:
        print(Roman[rom[i]])
        ans += Roman[rom[i]]
        print(ans)
    else:
        ans -= Roman[rom[i]]
        print(Roman[rom[i]])
        print(ans)
    p = Roman[rom[i]]
        
 
print(ans)
