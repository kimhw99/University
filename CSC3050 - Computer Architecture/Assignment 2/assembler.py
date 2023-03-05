from register import register
from binaryConversion import complementVector
from binaryConversion import binVector
from phase1 import fullCode

#Converts R Type Instructions into Binary
def modeR(code):

    #clean up code

    while code.find("\t")!=-1:
        code=code.replace("\t","")
        
    while code.find("  ")!=-1:
        code=code.replace("  "," ")

    while code[0]==" ":
        code=code[1:]

    while code[-1]==" ":
        code=code[:-1]
    
    output=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alf = code[0:code.find(" ")]

    #rd_rs_rt
    rd_rs_rt = ["add","addu","and","nor","or","slt","sltu","sub","subu","xor"]
    rd_rs_rt_func = [[1,0,0,0,0,0],[1,0,0,0,0,1],[1,0,0,1,0,0],[1,0,0,1,1,1],[1,0,0,1,0,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,0,0,0,1,0],[1,0,0,0,1,1],[1,0,0,1,1,0]]
    
    if alf in rd_rs_rt:
        output[16:21] = register(code[code.find(" "):code.find(",")]) #rd
        output[6:11] = register(code[code.find(","):code.find(",",code.find(",")+1)]) #rs
        output[11:16] = register(code[code.find(",",code.find(",")+1):]) #rt
        output[26:] = rd_rs_rt_func[rd_rs_rt.index(alf)] #func
    
    #rs_rt
    rs_rt = ["div","divu","mult","multu"]
    rs_rt_func = [[0,1,1,0,1,0],[0,1,1,0,1,1],[0,1,1,0,0,0],[0,1,1,0,0,1]]

    if alf in rs_rt: 
        output[6:11] = register(code[code.find(" "):code.find(",")]) #rs
        output[11:16] = register(code[code.find(","):]) #rt
        output[26:] = rs_rt_func[rs_rt.index(alf)] #func

    #rd_rs
    if alf == "jalr":
        output[16:21] = register(code[code.find(" "):code.find(",")]) #rd
        output[6:11] = register(code[code.find(","):]) #rs
        output[26:] = [0,0,1,0,0,1] #func
        
    #rs_
    rs_=["jr","mthi","mtlo"]
    rs_func = [[0,0,1,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,1]]
    
    if alf in rs_:
        output[6:11] = register(code[code.find(" "):]) #rs
        output[26:] = rs_func[rs_.index(alf)] #func

    #rd_
    rd_=["mfhi","mflo"]
    rd_func=[[0,1,0,0,0,0],[ 0,1,0,0,1,0]]

    if alf in rd_:
        output[16:21] = register(code[code.find(" "):code.find(",")]) #rd
        output[26:] = rd_func[rd_.index(alf)] #func

    #rd_rt_sa
    rd_rt_sa=["sll","sra","srl"]
    rd_rt_sa_func=[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0]]

    if alf in rd_rt_sa:
        output[16:21] = register(code[code.find(" "):code.find(",")]) #rd
        output[11:16] = register(code[code.find(","):code.find(",",code.find(",")+1)]) #rt
        output[21:26] = binVector(code[code.find(",",code.find(",")+1):],5) #sa
        output[26:] = rd_rt_sa_func[rd_rt_sa.index(alf)] #func

    #rd_rt_rs
    rd_rt_rs = ["sllv","srav","slrv"]
    rd_rt_rs_func = [[0,0,0,1,0,0],[0,0,0,1,1,1],[0,0,0,1,1,0]]

    if alf in rd_rt_rs:
        output[16:21] = register(code[code.find(" "):code.find(",")]) #rd
        output[11:16] = register(code[code.find(","):code.find(",",code.find(",")+1)]) #rt
        output[6:11] = register(code[code.find(",",code.find(",")+1):]) #rs
        output[26:] = rd_rt_rs_func[rd_rt_rs.index(alf)] #func

    #syscall
    if alf == "syscal":
        output[26:] = [0,0,1,1,0,0] #func

    output=str(output)
    output=output.replace(",","")
    output=output.replace(" ","")
    return(output[1:-1])



#Converts I Type Instructions into Binary
def modeI(code):

    #clean up code
    while code.find("  ")!=-1:
        code=code.replace("  "," ")

    while code.find("\t")!=-1:
        code=code.replace("\t","")

    while code[0]==" ":
        code=code[1:]

    while code[-1]==" ":
        code=code[:-1]
    
    output=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alf = code[0:code.find(" ")]

    #rt_rs_immediate
    rt_rs_immediate = ["addi","addiu","andi","ori","slti","sltiu","xori"]
    rt_rs_immediate_opc = [[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,1,1,0,0],[0,0,1,1,0,1],[0,0,1,0,1,0],[0,0,1,0,1,1],[0,0,1,1,1,0],[1,0,0,0,1,0],[1,0,0,1,1,0],[1,0,1,0,1,0],[1,0,1,1,1,0]]

    if alf in rt_rs_immediate:
        output[:6] = rt_rs_immediate_opc[rt_rs_immediate.index(alf)] #opcode
        output[11:16] = register(code[code.find(" "):code.find(",")])#rt
        output[6:11] = register(code[code.find(","):code.find(",",code.find(",")+1)])#rs
        output[16:] = binVector(code[code.find(",",code.find(",")+1):],16)#immediate
        
    #rt_immediate_rs
    rt_immediate_rs = ["lwl","lwr","swl","swr","lb","lbu","lh","lhu","lw","sb","sh","sw"]
    rt_immediate_rs_opc = [[1,0,0,0,1,0],[1,0,0,1,1,0],[1,0,1,0,1,0],[1,0,1,1,1,0],[1,0,0,0,0,0],[1,0,0,1,0,0],[1,0,0,0,0,1],[1,0,0,1,0,1],[1,0,0,0,1,1],[1,0,1,0,0,0],[1,0,1,0,0,1],[1,0,1,0,1,1]]
    
    if alf in rt_immediate_rs:
        output[:6] = rt_immediate_rs_opc[rt_immediate_rs.index(alf)] #opcode
        output[11:16] = register(code[code.find(" "):code.find(",")])#rt
        output[6:11] = register(code[code.find("("):code.find(")")])#rs
        output[16:] = binVector(code[code.find(","):code.find("(")],16)#immediate

    #rt_immediate
    rt_immediate=["lui"]
    rt_immediate_opc = [[0,0,1,1,1,1]]
    
    if alf in rt_immediate:
        output[:6] = rt_immediate_opc[rt_immediate.index(alf)] #opcode
        output[11:16] = register(code[code.find(" "):code.find(",")])#rt
        output[16:] = binVector(code[code.find(","):],16)#immediate

    output=str(output)
    output=output.replace(",","")
    output=output.replace(" ","")
    return(output[1:-1])



#Converts I Type Instructions (That contain Labels) into Binary
def modeI_label(code,fullCode,n):

    #clean up code

    while code.find("\t")!=-1:
        code=code.replace("\t","")
    
    while code.find("  ")!=-1:
        code=code.replace("  "," ")

    while code[0]==" ":
        code=code[1:]

    while code[-1]==" ":
        code=code[:-1]

    output=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alf = code[0:code.find(" ")]

    #rs_label
    rs_label = ["bgez","bgtz","blez","bltz"]
    rs_label_opc = [[0,0,0,0,0,1],[0,0,0,1,1,1],[0,0,0,1,1,0],[0,0,0,0,0,1]]

    if alf in rs_label:
        label=code[code.find(","):]
        label=label.replace(",","")
        label=label.replace(" ","")

        addressCurrent=int(n)
        addressTarget=0

        for i in fullCode[:n]:
            if i.find(":")!=-1:
                addressCurrent=addressCurrent-1

        for i in fullCode:
            if i.find(":")==-1:
                addressTarget=addressTarget+1
            
            if i==label+":":
                break

        output[:6]  = rs_label_opc[rs_label.index(alf)]#opcode
        output[6:11] = register(code[code.find(" "):code.find(",")])#rs
        output[16:] = (binVector(addressTarget-addressCurrent-1,16))#label

    #rs_rt_label
    rs_rt_label = ["beq","bne"]
    rs_rt_label_opc = [[0,0,0,1,0,0],[0,0,0,1,0,1]]

    if alf in rs_rt_label:
        label=code[code.find(",",code.find(",")+1):]
        label=label.replace(",","")
        label=label.replace(" ","")

        addressCurrent=int(n)
        addressTarget=0

        for i in fullCode[:n]:
            if i.find(":")!=-1:
                addressCurrent=addressCurrent-1

        for i in fullCode:
            if i.find(":")==-1:
                addressTarget=addressTarget+1
            
            if i==label+":":
                break
    
        output[:6]  = rs_rt_label_opc[rs_rt_label.index(alf)]#opcode
        output[6:11] = register(code[code.find(" "):code.find(",")])#rs
        output[11:16] = register(code[code.find(","):code.find(",",code.find(",")+1)])#rt
        output[16:] = (binVector(addressTarget-addressCurrent-1,16))#label
        
    output=str(output)
    output=output.replace(",","")
    output=output.replace(" ","")
    return(output[1:-1])



#Converts J Type Instructions into Binary
def modeJ(code, fullCode):

    #clean up code

    while code.find("\t")!=-1:
        code=code.replace("\t","")
    
    while code.find("  ")!=-1:
        code=code.replace("  "," ")

    while code[0]==" ":
        code=code[1:]

    while code[-1]==" ":
        code=code[:-1]

    output=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alf = code[0:code.find(" ")]

    label=code[code.find(" ",code.find(",")+1):]
    label=label.replace(",","")
    label=label.replace(" ","")

    address=1048576 #(=4194304/4 | 4194304 = 0x400000)
    
    for i in fullCode:
        if i.find(":")==-1:
            address=address+1
            
        if i==label+":":
            break

    if alf=="j":
        output[:6]=[0,0,0,0,1,0]
        output[6:]=(binVector(address,26)) #label
        
    elif alf=="jal":
        output[:6]=[0,0,0,0,1,1]
        output[6:]=(binVector(address,26))
    
    output=str(output)
    output=output.replace(",","")
    output=output.replace(" ","")
    return(output[1:-1])
