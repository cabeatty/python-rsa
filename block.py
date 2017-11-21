ind =  ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
alph = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def st2bv(input):
    input, inter, output = list(''.join(e for e in input.upper() if e.isalnum())), [], []
    for i in range(len(input)):
        for j in range(len(alph)):
            if (input[i] == alph[j]):
                inter.append(ind[j])
    for i in range(0, len(inter)-1, 2):
        output.append(inter[i] + inter[i+1])
    if ( len(inter)%2 == 1 ):
        output.append( "00" + inter[len(inter)-1] )
    for i in range( len(output) ):
        output[i] = int(output[i])
    return output



def bv2st(input):
    inter, output = [], []
    for i in range(len(input)):
        temp = str(input[i])
        while ( len(temp) != 4 ):
            temp = "0" + temp
        f, s = temp[0] + temp[1], temp[2] + temp[3]
        inter.append(f)
        inter.append(s)
    for i in range(len(inter)):
        for j in range(len(ind)):
            if (inter[i] == ind[j]):
                output.append(alph[j])
    return output
