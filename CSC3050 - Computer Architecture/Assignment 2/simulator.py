from phase2 import main

def adder(a, b): #adder
    #input : 32 bit address
    #output : 32 bit address +4
    a = bin(int(a,2) + int(b,2))[2:]
    while len(a)<32:
        a='0'+a

    a=a[-32:]
    return a

def shiftLeft(a, n): #binary 32 bit -> shift left 2
    return a[2:] + '0'*n

#mipsToBinary

def andGate(a, b):
    if int(a)==1 and int(b)==1:
        return 1

    else:
        return 0

def mux(input0, input1, switch):
    if switch==0:
        return input0
    elif switch==1:
        return input1



class mainControl: #Control - determines opcode stuff
    def __init__(self):
        self.regDst=0#Determines if 3 registers are used (some R types) (regWrite MUX)
        self.jump=0
        self.branch=0
        self.memRead=0 #-----Notify Data Memory
        self.memToReg=0 #Data Memory MUX
        self.aluOp=0 # Determines if instruction has ALU Operation (arithmatic) (Enables ALU Control) - 2 bit line?
        self.memWrite=0 #------Notify Data Memory
        self.aluSrc=0 #ALU MUX
        self.regWrite=0 #Notify regWrite that data will be written - write enable

    def control(self,a):
        #input : 6 bit opcode string
        #output : all the directories determined either 0 or 1

        if a=='000000': #R type
            self.regDst = 1
            self.jump = 0
            self.branch = 0
            self.memRead = 0
            self.memToReg = 0
            self.aluOp = '10'
            self.memWrite = 0
            self.aluSrc = 0
            self.regWrite = 1

        elif a in ['101011','101001','101000','101010','101110']: #store
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 0
            self.memToReg = 0
            self.aluOp = '00'
            self.memWrite = 1
            self.aluSrc = 1
            self.regWrite = 0

        elif a in ['100011','100101','100001',' 100100','100000','100010','100110']: #load
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 1
            self.memToReg = 1
            self.aluOp = '00'
            self.memWrite = 0
            self.aluSrc = 1
            self.regWrite = 1

        elif a in ['000100','000001','000111','000110','000001','000101']: #branch
            self.regDst = 0
            self.jump = 0
            self.branch = 1
            self.memRead = 0
            self.memToReg = 0
            self.aluOp = '01'
            self.memWrite = 0
            self.aluSrc = 0
            self.regWrite = 0

        elif a in ['000010','000011']: #jump j
            self.regDst = 0
            self.jump = 1
            self.branch = 0
            self.memRead = 0
            self.memToReg = 0
            self.aluOp = '00'
            self.memWrite = 0
            self.aluSrc = 0
            self.regWrite = 0

        elif a in ['001000','001001','001100','001101',' 001110','001010','001011','001111']: # 50% of i types
            self.regDst = 0
            self.jump = 0
            self.branch = 0
            self.memRead = 0
            self.memToReg = 0
            self.aluOp = '00'
            self.memWrite = 0
            self.aluSrc = 1
            self.regWrite = 1



def vectorBin(a, n):#take a vector 'a', reverse it, return its 'n' bit binary form in string
    a.reverse()
    for i in range(0,len(a)):
        x=bin(a[i])
        x=x[2:]
        a[i]=x

    for i in range(0,len(a)):
        while len(a[i]) != int(n/len(a)):
            a[i]='0'+ a[i]

    result=''
    for i in a:
        result=result+i
            
    return result


def binDecVector(a): #32 bit string binary a -> vector of 4 elements
    d0=int(a[0:8],2)
    d1=int(a[8:16],2)
    d2=int(a[16:24],2)
    d3=int(a[24:32],2)
    
    return [d3,d2,d1,d0]


def signDec(a): #signed binary to decimal
    if a[0]=='1':
        a=a.replace('1','2')
        a=a.replace('0','1')
        a=a.replace('2','0')
        a=int(a,2)*-1 -1

    elif a[0]=='0':
        a=int(a,2)

    return a

def decSign(a,n): #decimal a to signed binary with n bits
    b = abs(a)
    
    if a!=b:
        b=bin(b-1)[2:]
        b=b.replace('1','2')
        b=b.replace('0','1')
        b=b.replace('2','0')
        while len(b)!=n:
            b='1'+b

    elif a==b:
        b=bin(b)[2:]
        while len(b)!=n:
            b='0'+b

    return b
    

class regWrite: #regWrite
    def __init__(self , rr1 , rr2 , wr , wd , switch, registerMemory, instruction): #5bit bin string / 5bit bin string / 5bit bin string / 32bit bin data (after processing) / int 1 or 0
        #Inputs
        self.rr1=rr1 # (rs)
        self.rr2=rr2 # (rt)
        self.wr=wr #write register (rd)
        self.wd=wd #write data
        self.we=switch #write enable - control.regWrite()
        self.regMemory=registerMemory
        self.instruction = instruction #input data

        #Outputs (data from register) (read data)
        self.rd1='' 
        self.rd2=''

        # Activate
        # readData()
        # after read data from data memory mux comes back
        # if write enable (regWrite) = 1, writeData() 
    
    def readData(self):

        b=self.regMemory


        if self.instruction[:6]+self.instruction[26:]=='000000001100': #syscall
            self.rd1 = vectorBin(b[2*4:2*4+4],32)
            if int(self.rd1,2)==1:
                self.rd2 = vectorBin(b[4*4:4*4+4],32) # a0 = integer (print_int)
            elif int(self.rd1,2)==4:
                self.rd2 = vectorBin(b[4*4:4*4+4],32) # a0 = string address (print_string)
            elif int(self.rd1,2)==5:
                self.rd2 = vectorBin(b[2*4:2*4+4],32) # integer in v0 (read_int)
            elif int(self.rd1,2)==8:
                self.rd2 = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32)] # a0 = start address, a1 = length (read_string)
            elif int(self.rd1,2)==9:
                self.rd2 = vectorBin(b[4*4:4*4+4],32) # (sbrk) - return address of data in a0 & put it in $v0
            elif int(self.rd1,2)==10:
                self.rd2 = "BREAK"# (exit)
            elif int(self.rd1,2)==11:
                self.rd2 = vectorBin(b[4*4:4*4+4],32) # a0 (print_char)
            elif int(self.rd1,2)==12:
                self.rd2 = vectorBin(b[2*4:2*4+4],32) # v0 (read_char)
            elif int(self.rd1,2)==13:
                self.rd2 = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# a0 filename / a1 flags / a2 mode (open)
            elif int(self.rd1,2)==14:
                self.rd2 = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# file desc / buffer / length (read)
            elif int(self.rd1,2)==15:
                self.rd2 = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# file desc / buffer / length (write)
            elif int(self.rd1,2)==16:
                self.rd2 = vectorBin(b[4*4:4*4+4],32) # (close) a0 file descriptor
            elif int(self.rd1,2)==17:
                self.rd2 = "BREAK"
                # exit2

        elif self.instruction[:6]+self.instruction[26:]=='000000010000': #mfhi
            self.rd1 = b[33*4:33*4+4]
            self.rd1=vectorBin(self.rd1, 32)

        elif self.instruction[:6]+self.instruction[26:]=='000000010010': #mflo
            self.rd1 = b[34*4:34*4+4]
            self.rd1=vectorBin(self.rd1, 32)
            
        elif self.instruction[:6]+self.instruction[26:]=='000000010001': #mthi
            self.wr = '100001'
            
        elif self.instruction[:6]+self.instruction[26:]=='000000010011': #mtlo
            self.wr = '100010'

        elif self.instruction[:6]+self.instruction[26:] in ['000000000000',' 0000000010','000000000011']: #sll, srl, sra
            self.rd1 = self.instruction[21:26]
            self.rd1 = b[int(self.rr1,2)*4:int(self.rr1,2)*4+4]
            self.rd1=vectorBin(self.rd1, 32)

        else:
            self.rd1 = b[int(self.rr1,2)*4:int(self.rr1,2)*4+4]
            self.rd2 = b[int(self.rr2,2)*4:int(self.rr2,2)*4+4]
            self.rd1=vectorBin(self.rd1, 32)
            self.rd2=vectorBin(self.rd2, 32)


    def writeData(self):
        b=self.regMemory

        if self.instruction[:6]+self.instruction[26:]=='000000011010': #div
            b[33*4:33*4+4]= binDecVector(self.wd[0]) #hi - quotient
            b[34*4:34*4+4]= binDecVector(self.wd[1]) #lo - remainder
            
        elif self.instruction[:6]+self.instruction[26:]=='000000011000': #mult
            b[33*4:33*4+4]= binDecVector(self.wd)
            b[34*4:34*4+4]= binDecVector(self.wd) #Hi & lo
            
        elif self.instruction[:6]+self.instruction[26:]=='000000001000': #jr
            b[32*4:32*4+4]= binDecVector(self.wd) #pc
            
        elif self.instruction[:6]+self.instruction[26:]=='000000001001': #jalr
            b[int(self.wr,2)*4:int(self.wr,2)*4+4] = binDecVector(self.wd[0])
            b[32*4:32*4+4]= binDecVector(self.wd[1]) #write register, pc register

        elif self.instruction[:6]=='10010': #lwl    
            b[int(self.wr,2)*4:int(self.wr,2)*4+2] = binDecVector(self.wd)

        elif self.instruction[:6]=='10110': #lwr
            b[int(self.wr,2)*4+2:int(self.wr,2)*4+4] = binDecVector(self.wd)

        elif self.wd in ['']:
            pass

        else:
            b[int(self.wr,2)*4:int(self.wr,2)*4+4] = binDecVector(self.wd)

        return b



class aluControl:
    def __init__(self, aluOP, func):
        #inputs
        self.aluOP = aluOP # 2 bit input from control (00, 01, 10, 11)
        self.func = func # 6 bit (from R command only)

        #output
        self.aluCont='' #4 bit binary -> ALU Control

        #Main Contol & R-type Control

    def contro1(self):
        self.aluCont=self.func

        if self.aluCont[:6]!='000000':
            self.aluCont = self.aluCont[:6]
        
    def control(self):
        if self.aluOP == '00':
            self.aluCont='0010' # lw / sw (=add)

        elif self.aluOP[0]+self.func[2:]=='10000':
            self.aluCont='0010' # add

        elif self.aluOP[0]+self.func[2:]=='10010':
            self.aluCont='0110' # subtract

        elif self.aluOP[0]+self.func[2:]=='10100':
            self.aluCont='0000' # AND

        elif self.aluOP[0]+self.func[2:]=='10101':
            self.aluCont='0001' # OR

        elif self.aluOP[0]+self.func[2:]=='11010':
            self.aluCont='0111' # set on less than

        elif self.aluOP[1]=='1':
            self.aluCont='0110' # Branch Equal



class ALU:
    def __init__(self, rd1, rd2, aluCont, pc, memory):
        #inputs (2 32 bit binary data from regWrite, function code)
        self.rd1= rd1 
        self.rd2= rd2
        self.aluCont = aluCont #output from ALU control 
        self.pc = pc
        self.memory = memory

        #outputs
        self.zero=0 #toggles to 1 if result is 0
        self.result='' #32 bit result of operation

    def aluResult(self):
        #print(self.aluCont)
        self.zero=0
        
        if self.aluCont in ['000000100000','0010','001000']: #add, addi signed
            if (signDec(self.rd1) + signDec(self.rd2) >= -2**31) and (signDec(self.rd1) + signDec(self.rd2) < 2**31-1):
                self.result = decSign(signDec(self.rd1) + signDec(self.rd2),32)
                
        #####################################################
        elif self.aluCont in ['000000001100']: #syscall

            #test.in - read
            #test.out - print

            print(self.rd2)
            
            if int(self.rd1,2)==1:
                self.result = int(self.rd2,2) # a0 = integer (print_int)
                
                f = open('test.out','r')
                g = f.read()
                f.close()

                f = open('test.out','w')
                f.write(str(self.result))
                f.write(g)
                f.close()

            elif int(self.rd1,2)==4:
                self.result = int(self.rd2,2)# a0 = string address (print_string)
                while self.memory[self.result] != 0:
                    f = open('test.out','r')
                    g = f.read()
                    f.close()

                    f = open('test.out','w')
                    f.write(chr(self.memory[self.result]))
                    f.write(g)
                    f.close()
                    self.result = self.result + 1
                
            elif int(self.rd1,2)==5:
                self.result = int(self.rd2,2) # integer in v0 (read_int)

                f = open('test.in','r')
                g = f.read()
                f.close()

                f = open('test.in','w')
                f.write(str(self.result))
                f.write(g)
                f.close()

            elif int(self.rd1,2)==8:
                self.result = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32)] # a0 = start address, a1 = length (read_string)

                addr = int(self.rd2[0],2)
                
                while t != int(self.rd2[1],2):
                    f = open('test.in','r')
                    g = f.read()
                    f.close()

                    f = open('test.in','w')
                    f.write(chr(self.memory[addr]))
                    f.write(g)
                    f.close()
                    t = t + 1
                
            elif int(self.rd1,2)==9:
                self.result = vectorBin(b[4*4:4*4+4],32) # (sbrk) - return address of data in a0 & put it in $v0
            elif int(self.rd1,2)==10:
                self.result = "BREAK"# (exit)
                
            elif int(self.rd1,2)==11:
                self.result = chr(int(self.rd2,2)) # a0 (print_char)

                f = open('test.out','r')
                g = f.read()
                f.close()

                f = open('test.out','w')
                f.write(str(self.result))
                f.write(g)
                f.close()
                
            elif int(self.rd1,2)==12:
                self.result = chr(int(self.rd2,2)) # v0 (read_char)

                f = open('test.in','r')
                g = f.read()
                f.close()

                f = open('test.in','w')
                f.write(str(self.result))
                f.write(g)
                f.close()
                
            elif int(self.rd1,2)==13:
                self.result = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# a0 filename / a1 flags / a2 mode (open)
            elif int(self.rd1,2)==14:
                self.result = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# file desc / buffer / length (read)
            elif int(self.rd1,2)==15:
                self.result = [vectorBin(b[4*4:4*4+4],32),vectorBin(b[5*4:5*4+4],32),vectorBin(b[6*4:6*4+4],32)]# file desc / buffer / length (write)
            elif int(self.rd1,2)==16:
                self.result = vectorBin(b[4*4:4*4+4],32) # (close) a0 file descriptor
            elif int(self.rd1,2)==17:
                self.result = "BREAK"# (exit)
                # exit2
            
        
        elif self.aluCont in ['000000100001','001001']: #add, addi unsigned
            self.result = bin(int(self.rd1,2) + int(self.rd2,2))[2:]
            while len(self.result)!=32:
                self.result='0'+self.result

        elif self.aluCont in ['0000','000000100100','001100']: #and, andi
            if self.aluCont in ['001100']:
                self.rd2='0000000000000000'+self.rd2[16:]
            
            for i in range(0,len(self.rd1)):
                    if (self.rd1[i]==self.rd2[i]=='1'):
                        self.result=self.result+'1'
                    else:
                        self.result=self.result+'0'

        elif self.aluCont in ['000000000000','000000000100']: #sll, sllv
            self.result = self.rd2 + int(self.rd1,2)*'0'
            self.result = self.result[-32:]

        elif self.aluCont in ['000000000010','000000000110']: #srl, srlv
            self.result = int(rd1)*'0' + self.rd2 
            self.result = self.result[-32:]

        elif self.aluCont in ['000000000011','000000000111']: #sra, srav
            self.result = int(rd1)*self.rd2[0] + self.rd2 
            self.result = self.result[-32:]
           
        elif self.aluCont in ['000000001001']: #jalr
            r=bin(int(self.pc,2)+8)[2:]
            while len(r)!=32:
                r='0'+r
            self.result = [r , self.rd1] #write register, pc register

        elif self.aluCont in ['000000001000']: #jr
            self.result = self.rd1 #rd1 data -> write to pc register



        #move from hi / lo ( Data : HI / LO -> rd )
        elif self.aluCont in ['000000010000','000000010010']: #mfhi, mflo
            self.result = self.rd1 #rd1 data -> write to HI / LO
        

        #move to hi / lo ( Data : rs -> HI / LO )
        elif self.aluCont in ['000000010001','000000010011']: #mthi, mtlo
            self.result = self.rd1 #rd1 data -> write to HI / LO



        #Div : quotient goes to HI(2nd last), remainder goes to LO (last) (list for 2 types?)

        elif self.aluCont in ['000000011010']: #Div
            if (signDec(self.rd1) + signDec(self.rd2) >= -2**31) and (signDec(self.rd1) + signDec(self.rd2) < 2**31-1):
                self.result = [decSign(int(signDec(self.rd1) / signDec(self.rd2)),32),decSign(int(signDec(self.rd1) % signDec(self.rd2)),32)]

        elif self.aluCont in ['000000011011']: #Divu
            q = bin(int(int(self.rd1,2) / int(self.rd2,2)))[2:]
            r = bin(int(int(self.rd1,2) % int(self.rd2,2)))[2:]
            print(q, r)
            while len(q)!=32:
                q='0'+q
            while len(r)!=32:
                r='0'+r

            self.result = [q,r]


        #mult : result goes to LO & HI (2nd last)
        elif self.aluCont in ['000000011000']: #signed mult
            if (signDec(self.rd1) + signDec(self.rd2) >= -2**31) and (signDec(self.rd1) + signDec(self.rd2) < 2**31-1):
                self.result = decSign(int(signDec(self.rd1) * signDec(self.rd2)),32)

        elif self.aluCont in ['000000011001']: #unsigned mult
            self.result = bin(int(int(self.rd1,2) * int(self.rd2,2)))[2:]
            while len(self.result)!=32:
                self.result='0'+self.result

        elif self.aluCont in ['000000100111']:
            for i in range(0,len(self.rd1)):
                    if (self.rd1[i]==self.rd2[i]=='0'):
                        self.result=self.result+'1'
                    else:
                        self.result=self.result+'0'

         
        #or
        elif self.aluCont in ['0001','000000100101', '001101']: #or, ori
            if self.aluCont in ['001101']:
                self.rd2='0000000000000000'+self.rd2[16:]
            
            for i in range(0,len(self.rd1)):
                    if (self.rd1[i]==self.rd2[i]=='0'):
                        self.result=self.result+'0'
                    else:
                        self.result=self.result+'1'

        #slt
        elif self.aluCont in ['0111','000000101010', '001010']: #slt, slti
            if signDec(self.rd1)<signDec(self.rd2): #signed compare
                self.result="00000000000000000000000000000001"
            else:
                self.result="00000000000000000000000000000000"

        elif self.aluCont in ['000000101011','sltiu','001011']: #unsigned compare
            if int(self.rd1,2)<int(self.rd2,2):
                self.result="00000000000000000000000000000001"
            else:
                self.result="00000000000000000000000000000000"

        elif self.aluCont in ['000000100010','0110']: #sub signed + overflow 
            if (signDec(self.rd1) + signDec(self.rd2) >= -2**31) and (signDec(self.rd1) + signDec(self.rd2) < 2**31-1):
                self.result = decSign(int(signDec(self.rd1) - signDec(self.rd2)),32)

        elif self.aluCont in ['000000100011']: #subu
            self.result = bin(int(self.rd1,2) - int(self.rd2,2))[2:]
            while len(self.result)!=32:
                self.result='0'+self.result

        elif self.aluCont in ['000000100110','001110']: #xor, xori
            if self.aluCont in ['001110']:
                self.rd2='0000000000000000'+self.rd2[16:]
                
            for i in range(0,len(self.rd1)):
                    if (int(self.rd1[i])+int(self.rd2[i])==1):
                        self.result=self.result+'1'
                    else:
                        self.result=self.result+'0'

        elif self.aluCont == '001111': #lui
            # immediate + 16 0's -----> sign extend & write to rt
            self.result=self.rd2 + '0000000000000000'

            self.result = self.result[-32:]

            while len(self.result)<16:
                self.result = '0'+self.result
            
            while len(self.result)!=32:
                self.result = self.result[0]+self.result

            self.result = self.result[-32:]
            

#-----------------------------------------------------------------------------------
                        
        #if data is 87654321 (hex)
        #ascii, asciiz uses big endian ( 87(0) 65(1) 43(2) 21(3) )
        #everything else uses little endian ( 12(0) 34(1) 56(2) 78(3) )

        #most   --------------   least
        #0 1    | 2 3 I 4 5 |    6 7 8
        # output : most significant byte of the four

#-----------------------------------------------------------------------------------

        #load
        elif self.aluCont in ['100000','100001']: #lb, lh
            self.result = decSign(int(self.rd1) + signDec(self.rd2),32)

        elif self.aluCont in ['100100','100101', '100011']: #lbu, lhu lw
            self.result = bin(int(self.rd1,2) + int(self.rd2,2))[2:]
            while len(self.result)!=32:
                self.result='0'+self.result

        elif self.aluCont in ['100010', '100110']: #lwl, lwr (load word left / right)
            self.result = decSign(int(self.rd1) + signDec(self.rd2),32)

        
        
        #store
        elif self.aluCont in ['101000','101001']: #signed
            self.result = decSign(int(self.rd1,2) + signDec(self.rd2),32)

        elif self.aluCont in ['101011']: #unsigned
            self.result = decSign(int(self.rd1,2) + int(self.rd2,2),32)
            while len(self.result)!=32:
                self.result='0'+self.result
 
        elif self.aluCont in ['101110','101010']: #swrl swl
            self.result = decSign(int(self.rd1) + signDec(self.rd2),32)
        #swl, swr (store word left / right)
        

        
        #branch
        elif self.aluCont in ['000100']: #beq
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs == rt, then branch to effective target address
            if int(rd1,2)==signDec(rd2):
                self.zero=1

        elif self.aluCont in ['000001']: #bgez
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs >= 0, then branch to effective target address
            if int(rd1,2)>=0:
                self.zero=1

        elif self.aluCont in ['000111']: #bgtz
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs > 0, then branch to effective target address
            if int(rd1,2)>0:
                self.zero=1

        elif self.aluCont in ['000110']: #blez
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs <= 0, then branch to effective target address
            if int(rd1,2)<=0:
                self.zero=1

        elif self.aluCont in ['000001']: #bltz
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs < 0, then branch to effective target address
            if int(rd1,2)<0:
                self.zero=1

        elif self.aluCont in ['000101']: #bne
            #16 bit immediate * 4 + initial address (branch target address)
            #if rs != rt, then branch to effective target address
            if int(self.rd1,2)!=signDec(self.rd2):
                self.zero=1

        if self.result=="00000000000000000000000000000000":
            self.zero=1



class dataMem: #dataMemory
    def __init__(self, address, writeData,  memRead, memWrite, datamem, opcfunc):
        # inputs
        self.address = address
        self.writeData = writeData
        self.memory = datamem
        self.opcfunc = opcfunc

        self.memRead = memRead # 1 / 0 Switch
        self.memWrite = memWrite # 1 / 0 Switch

        # Output
        self.readData = ''


    def load(self):     
        b=self.memory
        
        #self.address
        if self.opcfunc == '100000': #lb
            print("hello")
            self.readData = bin(b[int(int(self.address,2)/4)])[2:]

            while len(self.readData)<8:
                self.readData = '0'+self.readData
            
            while len(self.readData)!=32:
                self.readData = self.readData[0]+self.readData
                #binDecVector

        elif self.opcfunc=='read': #test
            for i in len(0,int(len(b)/4)):
                if b[i:i+4]!=[0,0,0,0]:
                    print(b[i:i+4], i)
            
        elif self.opcfunc == '100001': #lh
            x= bin(b[int(int(self.address,2)/4)+1])[2:]
            y= bin(b[int(int(self.address,2)/4)])[2:]

            while len(x)<8:
                x = '0'+x

            while len(x)!=24:
                x = x[0]+x

            while len(b)!=8:
                y = '0'+y

            self.readData = x+y
            #binDecVector


        elif self.opcfunc == '100100': #lbu
            self.readData = bin(b[int(int(self.address,2)/4)])[2:]
            
            while len(self.readData)!=32:
                self.readData = '0'+self.readData
                #binDecVector

        elif self.opcfunc == '100101': #lhu
            x= bin(b[int(int(self.address,2)/4)+1])[2:]
            y= bin(b[int(int(self.address,2)/4)])[2:]
                
            while len(x)!=24:
                x = '0'+a

            while len(b)!=8:
                y = '0'+y

            self.readData = x+y
            #binDecVector

        elif self.opcfunc == '100011': #lw
            x= bin(b[int(int(self.address,2)/4)+3])[2:]
            y= bin(b[int(int(self.address,2)/4)+2])[2:]
            z= bin(b[int(int(self.address,2)/4)+1])[2:]
            w= bin(b[int(int(self.address,2)/4)])[2:]

            while len(x)!=8:
                x = x[0]+x

            while len(y)!=8:
                y = '0'+y

            while len(z)!=8:
                z = '0'+z

            while len(w)!=8:
                w = '0'+w

            self.readData = x+y+z+w
            #binDecVector

        elif self.opcfunc == '100010': #lwl
            z= bin(b[int(int(self.address,2)/4)+1])[2:]
            w= bin(b[int(int(self.address,2)/4)])[2:]

            while len(z)!=8:
                z = z[0]+z

            while len(w)!=8:
                w = '0'+w

        elif self.opcfunc == '100110': #lwr
            x= bin(b[int(int(self.address,2)/4)+3])[2:]
            y= bin(b[int(int(self.address,2)/4)+2])[2:]
            
            while len(x)!=8:
                x = x[0]+x

            while len(y)!=8:
                y = '0'+y

    def write(self):
        b=self.memory

        if self.opcfunc == '101000': #sb
            b[int(int(self.address,2)/4)] = int(self.writeData[-8:],2)
            
        elif self.opcfunc == '101001': #sh
            b[int(int(self.address,2)/4)+1] = int(self.writeData[-8:],2)
            b[int(int(self.address,2)/4)] = int(self.writeData[-16:-8],2)

        elif self.opcfunc == '101011': #sw
            b[int(int(self.address,2)/4)+3] = int(self.writeData[-8:],2)
            b[int(int(self.address,2)/4)+2] = int(self.writeData[-16:-8],2)
            b[int(int(self.address,2)/4)+1] = int(self.writeData[8:16],2)
            b[int(int(self.address,2)/4)] = int(self.writeData[:8],2)
            
        elif self.opcfunc == '101110': #swr
            b[int(int(self.address,2)/4)+1] = int(self.writeData[8:16],2)
            b[int(int(self.address,2)/4)] = int(self.writeData[:8],2)
            
        elif self.opcfunc == '101010': #swl
            b[int(int(self.address,2)/4)+3] = int(self.writeData[-8:],2)
            b[int(int(self.address,2)/4)+2] = int(self.writeData[-16:-8],2)

        return b


class PC:
    def __init__(self, register):
        self.register = register
        self.pc=''
        #PC is also stored in small endian

    def load(self):
        b = self.register
        self.pc = bin((b[32*4] + (16**2)*b[32*4+1] + (16**4)*b[32*4+2] + (16**6)*b[32*4+3])) #binary
        return self.pc 

    def write(self, value): #Binary Value -> write to register
        b = self.register
        b[32*4:32*4+4] = binDecVector(value)

        return b #register


class instructionMemory:
    def __init__(self, pc, binaryCode):
        self.binCode = binaryCode
        self.address = int((int(pc,2)-4194304)/4)

    def load(self): #loads binary code in the address
        vector=[]
        f = open(self.binCode, "r")
        
        for i in f:
            vector=vector+[i]

        vector = (vector[self.address])[:-1]

        #load all these
        self.control = vector[:6]
        self.reg1 = vector[6:11]
        self.reg2 = vector[11:16]
        self.writereg = vector[16:21]
        self.shift = vector[21:26]
        self.func = vector[26:]

        self.opcfunc = vector[:6]+vector[26:] #opcode + function 
        self.immediate = vector[16:] #branch / i type
        self.jump = vector[6:] #jump
        
        self.instruction = vector








#/simulator test.asm test.txt test_checkpoints.txt test.in test.out


#Input Files
#   test.asm - input code
#   test.txt - stores converted binary code
#   test_checkpoints.txt - file indicating file checkpoints
#   test.in - stores inputs for some read-related i/o operations
#   test.out - name of output file storing outputs for print related i/o operations


#Computer Parts
#   simulator_pc - PC
#   simulator_instmem - Instruction Memory
#   adder() - Adders (+4)
#   mux() - multiplexer
#   simulator_main - Main Control
#   simulator_register - regWrite
#   simulator_aluControl - ALU Control
#   simulator_alu - ALU
#   simulator_datamemory - Data Memory


#Keep Track
#   registserMemory - Register Memory
#   dataMemory - Data Memory
#   pc - PC
#   simulator_instmem.instruction - Current Binary Instruction


###Initialize
registerMemory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 80, 0, 0, 0, 160, 0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0]

dataMemory = [0]*10485760 #~A00000

pc='10000000000000000000000'

inputCode = 'test.asm'

binaryCode = 'test.txt'

check=open('test_checkpoints.txt','r')
checkpoints=[]
for i in check:
    checkpoints=[int(i)]+checkpoints
check.close

###Mips -> Binary
main(inputCode, binaryCode)

vector=[]
f = open(binaryCode, "r")
for i in f:
    vector = vector+[i]




###.data (.data), .text (Binary Code) -> Memory

    #.text
f=open(binaryCode,'r')
g=[]

for i in f:
    i=i.replace("\n","")
    g=g+[i]

h=int(int('400000',16)) #.text pos
for i in g:
    i=binDecVector(i)
    dataMemory[h:h+4]=i
    h=h+4


    #.data
f=open(inputCode,'r')
g=[]

for i in f:
    i=i[:i.find("#")]
    i=i.replace("\n","")
    g = g+[i]

g=g[1:g.index('.text')]
g.remove('')

j = int(int('500000',16)) #.data position
for i in g:
    datName = i[:i.find(":")+1]
    datType = i[i.find("."):int(i.find(" ",int(i.find(" ")+1)))]
    datData = i[int(i.find(" ",int(i.find(" ")+1)))+1:]

    if datType =='.word':
        while j%4!=0:
            j=j+1
        
        datData = bin(int(datData))[2:]
        while len(datData)!=32:
            datData='0'+datData
        datData = binDecVector(datData)
        dataMemory[j:j+4]=datData
        j=j+4

    elif datType =='.half':
        while j%2!=0:
            j=j+1
        
        datData = bin(int(datData))[2:]
        while len(datData)<32:
            datData='0'+datData
        datData = binDecVector(datData)[2:]
        dataMemory[j:j+2]=datData
        j=j+2

    elif datType =='.byte':
        datData = bin(int(datData))[2:]
        while len(datData)<8:
            datData = '0'+datData
        dataMemory[j]=datData
        j=j+1

    elif dataType == '.ascii':
        for i in range(0,len(datData)):
            dataMemory[j]=ord(datData[i])
            j=j+1

    elif dataType == '.asciiz':
        j=j+1
        for i in range(0,len(datData)):
            dataMemory[j]=ord(datData[i])
            j=j+1


###Single Cycle
while int((int(pc,2)-4194304)/4) < len(vector):
    
    # PC -> outputs PC
    simulator_pc = PC(registerMemory) # PC
    pc = simulator_pc.load()
    
    if int((int(pc,2) - 4194304)/4) in checkpoints:
        checkRegister=open('register_%s.bin' %int((int(pc,2) - 4194304)/4) ,'bw+')
        checkRegister.write(bytes(registerMemory))
        
        checkMemory=open('memory_%s.bin' %int((int(pc,2) - 4194304)/4) ,'bw+')
        checkMemory.write(bytes(dataMemory))

        checkMemory.close()
        checkRegister.close()
        print(int(pc,2) - 4194304)
        

    # Instruction Memory
    simulator_instmem = instructionMemory(pc, binaryCode) # Instruction Memory
    simulator_instmem.load()

    # Main Control
    simulator_main = mainControl() #Main Control
    simulator_main.control(simulator_instmem.control) 

    # Registers - regWrite
    simulator_register = regWrite(simulator_instmem.reg1 , simulator_instmem.reg2 , mux(simulator_instmem.reg2 , simulator_instmem.writereg , simulator_main.regDst) , '' , simulator_main.regWrite, registerMemory, simulator_instmem.instruction)
    simulator_register.readData()

    # Sign Extension - 16 bit -> 32 Bit
    extendedImmediate = simulator_instmem.immediate

    while len(extendedImmediate)!=32:
        extendedImmediate = extendedImmediate[0]+extendedImmediate

    # ALU Control
    simulator_aluControl = aluControl(simulator_main.aluOp,simulator_instmem.opcfunc)
    simulator_aluControl.contro1()

    # ALU Main
    simulator_alu = ALU(simulator_register.rd1 , mux(simulator_register.rd2 , extendedImmediate , simulator_main.aluSrc) , simulator_aluControl.aluCont, pc, registerMemory)
    simulator_alu.aluResult()

    # Data Memory
    simulator_datamemory = dataMem(simulator_alu.result , simulator_register.rd2 , simulator_main.memRead, simulator_main.memWrite , dataMemory , simulator_instmem.opcfunc )

    if simulator_main.memRead == 1:
        simulator_datamemory.load()

    if simulator_main.memWrite == 1:
        dataMemory = simulator_datamemory.write()

    # Write data
    mux(simulator_alu.result , simulator_datamemory.readData , simulator_main.memToReg)
    simulator_register = regWrite(simulator_instmem.reg1 , simulator_instmem.reg2 , mux(simulator_instmem.reg2 , simulator_instmem.writereg , simulator_main.regDst) , mux(simulator_alu.result , simulator_datamemory.readData , simulator_main.memToReg) , simulator_main.regWrite, registerMemory, simulator_instmem.instruction)

    if simulator_main.regWrite == 1:
        if (simulator_instmem.instruction != '00000000000000000000000000001100'):
            if (simulator_alu.result not in ['BREAK','']):
                registerMemory = simulator_register.writeData()

    # PC = PC + 4
    pc = adder(pc, '100') #32 bit pc + 4 output

    # shift left 2
    pcBranch = adder(pc, shiftLeft(extendedImmediate, 2))
    pcJump = pc[:6] + shiftLeft(simulator_instmem.jump, 2)

    # pc, pcBranch or pcJump
    pc = mux(mux(pc, pcBranch, andGate(simulator_main.branch,simulator_alu.zero)),pcJump,simulator_main.jump)
    registerMemory = simulator_pc.write(pc)
    print(hex(int(pc,2)), 'clear')


#Memory
for i in range(0,int(len(dataMemory)/4)):
    if dataMemory[4*i:4*i+4] != [0,0,0,0]:
        print(dataMemory[4*i:4*i+4], i-1048576, i)

file = open('memory_0.bin','br')
file = file.read()
file=list(file)

print('')

for i in range(0,int(len(file)/4)):
    if file[4*i:4*i+4] != [0,0,0,0]:
        print(file[4*i:4*i+4], i)

print('---------------------')

#Memory
for i in range(0,int(len(registerMemory)/4)):
    if registerMemory[4*i:4*i+4] != [0,0,0,0]:
        print(registerMemory[4*i:4*i+4], i)

file = open('register_0.bin','br')
file = file.read()
file=list(file)

print('')

for i in range(0,int(len(file)/4)):
    if file[4*i:4*i+4] != [0,0,0,0]:
        print(file[4*i:4*i+4], i)












