from phase1 import fullCode
from labelTable import labelTable
from mipsToBinary import mipsToBinary


def main(test_file, output_file):

    #phase1
    print("\nReduced MIPS (phase1)")
    test_file=fullCode(test_file)
    for i in range(0, len(test_file)):
        print(test_file[i])
        
    print("\n")

    #labelTable
    label_table=labelTable(test_file)

    #phase2
    print("Binary (phase2)")
    test_file=mipsToBinary(test_file)

    output_file=open(output_file,"w")
    
    for i in range(0, len(test_file)):
                   print (test_file[i])
                   output_file.write(test_file[i])
                   
                   if i!=len(test_file)-1:
                       output_file.write("\n")
                       
    output_file.close()
    print("\n")
    return test_file
