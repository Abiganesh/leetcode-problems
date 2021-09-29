digit="234"
alphabet={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
comblist=[]
final=[]
if(len(digit)==0):
    print(final)
elif(len(digit)==1):
    value=alphabet[digit]
    for alpha in value:
        final.append(alpha)
    print(final)
elif(len(digit)==2):
    for i in range(len(digit)):
        value=alphabet[digit[i]]
        comblist.append(value)
    
    
    for val in range(len(comblist[0])):
        for anval in range(len(comblist[1])):
            final.append(comblist[0][val]+comblist[1][anval])
            
     
    print(final)
elif(len(digit)==3):
    for i in range(len(digit)):
        value=alphabet[digit[i]]
        comblist.append(value)
    for val in range(len(comblist[0])):
        for anval in range(len(comblist[1])):
            for ananval in range(len(comblist[2])):
                final.append(comblist[0][val]+comblist[1][anval]+comblist[2][ananval])
    print(final)
else:
     for i in range(len(digit)):
        value=alphabet[digit[i]]
        comblist.append(value)
     for val in range(len(comblist[0])):
        for anval in range(len(comblist[1])):
            for ananval in range(len(comblist[2])):
                for four in range(len(comblist[3])):
                    final.append(comblist[0][val]+comblist[1][anval]+comblist[2][ananval]+comblist[2][four])
     print(final)
    
    
        
        

    
