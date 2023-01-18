import const

def genNonDetSubsetSumFunctionLocationMatrix(input_size):
    L=[]
    zeros = [0] * int(2*input_size + 5)
    for i in range(input_size):
        tempList = zeros.copy()
        tempList[i] = 1
        L.append(tempList)
        L.append(tempList)
        
    for i in range(input_size, 2*input_size):
        tempList = zeros.copy()
        tempList[i] = 1
        L.append(tempList)
        
    tempList = zeros.copy()
    tempList[2*input_size] = 1
    L.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+1] = 1
    L.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+2] = 1
    L.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+3] = 1
    L.append(tempList)
    
    #tempList = zeros.copy()
    #tempList[(2*input_size)+4] = 1
    #L.append(tempList)
    
    return L

def genNonDetSubsetSumFunctionMatrix(input_size):
    F=[]
    zeros = [0] * int(2*input_size + 5)
    
    #Function matrix for input neurons
    # functions 0 to 2n-1
    for i in range(input_size):
        tempListPos = zeros.copy()
        tempListNeg = zeros.copy()
        tempListPos[i] = 1
        tempListNeg[i] = -1
        F.append(tempListPos)
        F.append(tempListNeg)
        
    #Function matrix for sums of inputs 
    for i in range(input_size, 2*input_size):
        tempList = zeros.copy()
        tempList[i] = 1
        F.append(tempList)
        
    tempList = zeros.copy()
    tempList[2*input_size] = -1
    F.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+1] = 1
    F.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+2] = -1
    F.append(tempList)
    
    tempList = zeros.copy()
    tempList[(2*input_size)+3] = 1
    F.append(tempList)
    
    #tempList = zeros.copy()
    #F.append(tempList)
    return F
    
def genNonDetSubsetSumNoFunc(input_size):
    zeros = [0] * int((2*input_size)+5)
    zeros[(2*input_size)+5-1] = 1
    return zeros
    
def genNonDetSubsetThresholdMatrix(input_size):

    zeros = [0] * int((3*input_size)+5)
    T = zeros.copy()
    has_Threshold = zeros.copy()
    
    T[(3*input_size)+2] = -1
    has_Threshold[(3*input_size)+2] = 1
    
    T[(3*input_size)+3] = 1
    has_Threshold[(3*input_size)+3] = 1
    
    for i in range (2*input_size,3*input_size):
        has_Threshold[i] = 1
        

    return T,has_Threshold

 
def genNonDetSubsetSynapseList(input_size):

    syn = []
    num_combi = (2**input_size) - 1
    
    for i in range(input_size):
        syn.append((i,input_size+i))
        syn.append((input_size+i,(2*input_size)+2))
    
    syn.append((2*input_size,2*input_size+1))
    
    syn.append((2*input_size+1,2*input_size+2))
    
    syn.append((2*input_size+2,2*input_size+3))
    
    syn.append((2*input_size+3,2*input_size+4))
    
    #syn.append((2*input_size+4,2*input_size+5))
    return syn
    
    
       
def genNonDetConfiguration(S,SUM,input_size):
    zeros = [0] * int((2*input_size)+5)
    C = zeros.copy()
    for i in range(len(S)):
        if i < len(S):
            C[i] = S[i]
    C[2*input_size] = SUM+1
    return C
    
