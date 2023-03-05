from assembler import modeR
from assembler import modeI
from assembler import modeI_label
from assembler import modeJ

def mipsToBinary(fullCode):
    #TODO
    a=[]    #only for checking, can remove, output to a file?
    for i in range(0, len(fullCode)):
        code=fullCode[i]
    
        if code[:code.find(" ")] in ["j","jal"]:
            #print(modeJ(code,fullCode))
            a=a+[str(modeJ(code,fullCode))]
            #a=a+str(modeJ(code,fullCode))
        elif code[:code.find(" ")] in ["beq","bne","bgez","bgtz","blez","bltz"]:
            #print(modeI_label(code,fullCode,i))
            a=a+[str(modeI_label(code,fullCode,i))]
            #a=a+str(modeI_label(code,fullCode,i))
        elif code[:code.find(" ")] in ["lui","lb","lbu","lh","lhu","lw","sb","sh","sw","addi","addiu","andi","ori","slti","sltiu","xori","lwl","lwr","swl","swr"]:
            #print(modeI(code))
            a=a+[str(modeI(code))]
            #a=a+str(modeI(code))
        elif code[:code.find(" ")] in ["jalr","syscal","sllv","srav","slrv","sll","sra","srl","mfhi","mflo","jr","mthi","mtlo","div","divu","mult","multu","add","addu","and","nor","or","slt","sltu","sub","subu","xor"]:
            #print(modeR(code))
            a=a+[str(modeR(code))]
            #a=a+str(modeR(code))
            
    return a
