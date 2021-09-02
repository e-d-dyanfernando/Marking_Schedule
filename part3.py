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

progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
total = 0

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
        
    total = total + 1

    if P==120:
        print('Progression Outcome = Progress')
        progress = progress + 1
        
    elif P==100:
        print('Progression Outcome = Progress(module trailer)')
        module_trailer = module_trailer + 1
        
    elif P==80 or P==60 or P==40 and D!=0 or P==20 and D>20 or P==0 and D>50:
        print('Progression Outcome = Do not Progress – module retriever')
        module_retriever = module_retriever + 1
        
    elif P==40 and F==80 or P==20 and F>70 or P==0 and F>70:
        print('Progression Outcome = Exclude')
        exclude = exclude + 1

    print('Would you like to enter another set of data?')
    option = input('Enter "y" for yes or "q" to quit and view results:')

    if(option == 'y'):
        continue
    if(option == 'q'):
        break

print('-----------------------------------------------------')
print('Horizontal Histogram')

print('Progress  ', end='')
print(progress,'  : ',end='')
print('*'*progress)

print('Trailer  ', end='')
print(module_trailer,'   : ',end='')
print('*'*module_trailer)

print('Retriever  ', end='')
print(module_retriever,' : ',end='')
print('*'*module_retriever)

print('Excluded  ', end='')
print(exclude,'  : ',end='')
print('*'*exclude)

print(total,'outcomes in total.')
print('-----------------------------------------------------')
