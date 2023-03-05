#Turns a vector of 0's and 1's into its 2's complement
def complementVector(vector):
    for i in range(0,len(vector)):
        if vector[i]==0:
            vector[i]=1
        elif vector[i]==1:
            vector[i]=0

    for i in range(1,len(vector)):
        if vector[-1*i]==1:
            vector[-1*i]=0
        elif vector[-1*i]==0:
            vector[-1*i]=1
            break
            
    return vector

#Takes an integer "value" & length "n", and converts it into a binary vector of length n. 
def binVector(value,n):

    vector=[]
    value=str(value)
    value=value.replace(",","")
    value=value.replace(" ","")
    
    value_int=int(value)
    value= str(bin(value_int))
    value=value.replace("-","")
    value=value[2:]

    for i in range(0,len(value)):
        vector.append(int(value[i]))

    while len(vector)!=n:
        vector=[0]+vector

    if value_int!=abs(value_int):
        vector=complementVector(vector)
        
    return vector

