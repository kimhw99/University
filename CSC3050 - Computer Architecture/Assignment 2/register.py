def register(alf):

    alf=alf.replace(",","")
    alf=alf.replace("(","")
    alf=alf.replace(")","")
    alf=alf.replace(" ","")
    
    if alf=="$zero":
        return [0,0,0,0,0]
    
    elif alf == "$at":
        return [0,0,0,0,1]
    
    elif alf == "$v0":
        return [0,0,0,1,0]
    elif alf == "$v1":
        return [0,0,0,1,1]
    
    elif alf == "$a0":
        return [0,0,1,0,0]
    elif alf == "$a1":
        return [0,0,1,0,1]
    elif alf == "$a2":
        return [0,0,1,1,0]
    elif alf == "$a3":
        return [0,0,1,1,1]
    
    elif alf == "$t0":
        return [0,1,0,0,0]
    elif alf == "$t1":
        return [0,1,0,0,1]
    elif alf == "$t2":
        return [0,1,0,1,0]
    elif alf == "$t3":
        return [0,1,0,1,1]
    elif alf == "$t4":
        return [0,1,1,0,0]
    elif alf == "$t5":
        return [0,1,1,0,1]
    elif alf == "$t6":
        return [0,1,1,1,0]
    elif alf == "$t7":
        return [0,1,1,1,1]
    
    elif alf == "$s0":
        return [1,0,0,0,0]
    elif alf == "$s1":
        return [1,0,0,0,1]
    elif alf == "$s2":
        return [1,0,0,1,0]
    elif alf == "$s3":
        return [1,0,0,1,1]
    elif alf == "$s4":
        return [1,0,1,0,0]
    elif alf == "$s5":
        return [1,0,1,0,1]
    elif alf == "$s6":
        return [1,0,1,1,0]
    elif alf == "$s7":
        return [1,0,1,1,1]
    
    elif alf == "$t8":
        return [1,1,0,0,0]
    elif alf == "$t9":
        return [1,1,0,0,1]
    
    elif alf == "$k0":
        return [1,1,0,1,0]
    elif alf == "$k1":
        return [1,1,0,1,1]
    
    elif alf == "$gp":
        return [1,1,1,0,0]
    elif alf== "$sp":
        return [1,1,1,0,1]
    elif alf in ["$s8","$fp"]:
        return [1,1,1,1,0]
    elif alf == "$ra":
        return [1,1,1,1,1]
    
    else:
       return ["something went wrong",0,0,0,0]

