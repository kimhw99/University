#remove useless lines & comments
def fullCode(file):
    vector=[]
    f = open(file, "r")
    for i in f:
        code=str(i)
        code=code.replace("\n","")
        code=code.replace("\t","")
        
        if code.find("#")!=-1:
            code=code[:code.find("#")]

        while code.find("  ")!=-1:
            code=code.replace("  "," ")

        if len(code)!=0:        
            while code[0]==" ":
                if code==" ":
                    break
                code=code[1:]

            while code[-1]==" ":
                if code==" ":
                    break
                code=code[:-1]
                
            if code!=" ":
                vector=vector+[code]
                
    vector = vector[vector.index(".text")+1:]

    return vector
