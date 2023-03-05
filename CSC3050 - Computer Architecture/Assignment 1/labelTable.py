def labelTable(vector):

    label=[]
    address=[]
    #Address Starts from 0x400000 (4194304 in Decimal, increase by 4)
    
    for i in range(0, len(vector)):
        line = vector[i]
        if line.find(":")!=-1:
            label=label+[line]

    for i in range(0, len(label)):
        a=0
        for j in vector:
            if j.find(":")==-1:
                a=a+1
            
            if j==label[i]:
                break

        a=hex(4*a+4194304)
        address=address+[a]
        
    print("Address (labelTable)")
    
    for i in range(0, len(label)):
        print("%s \t %s" %(address[i], label[i]))

    if len(address)==0:
        print("----------------")
        
    print("\n")

    return [label, address]
