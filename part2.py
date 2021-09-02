def DATAP(P):
    if(P not in [0,20,40,60,80,100,120]):
        return 'Out of range'
def DATAD(D):        
    if(D not in [0,20,40,60,80,100,120]):
        return 'Out of range'
def DATAF(F):        
    if(F not in [0,20,40,60,80,100,120]):
        return 'Out of range'
    
def Total(P,D,F):
    if(P+D+F != 120):
        return 'Total incorrect'
        
while True:
    try:
        P = int(input('Please enter your credits at pass:='))
        if (DATAP(P) == 'Out of range'):
            print("Out of range")
            continue
        
        D = int(input('Please enter your credit at defer:='))
        if (DATAD(D) == 'Out of range'):
            print("Out of range")
            continue
        
        F = int(input('Please enter your credit at fail:='))   
        if (DATAF(F) == 'Out of range'):
            print("Out of range")
            continue
        
        if(Total(P,D,F) == 'Total incorrect'):
            print("Total incorrect")
            continue
        
    except ValueError:
        print('Integer required')
        continue

    if P==120:
        print('Progression Outcome = Progress')
    elif P==100:
        print('Progression Outcome = Progress(module trailer)')
    elif P==80 or P==60 or P==40 and D!=0 or P==20 and D>20 or P==0 and D>50:
        print('Progression Outcome = Do not Progress – module retriever')
    elif P==40 and F==80 or P==20 and F>70 or P==0 and F>70:
        print('Progression Outcome = Exclude')
