# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Name: E.D.D. Fernando

# Student UoW ID: w1839054
# Student IIT ID: 20200473
  
# Date: 25th April 2021

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

Marks = ([120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120])

for i in range(len(Marks)):
    
    P = Marks[i][0]
    if (DATAP(P) == 'Out of range'):
        print("Out of range")
        continue
        
    D = Marks[i][1]
    if (DATAD(D) == 'Out of range'):
        print("Out of range")
        continue

    F = Marks[i][2]   
    if (DATAF(F) == 'Out of range'):
        print("Out of range")
        continue
        
    if(Total(P,D,F) == 'Total incorrect'):
            print("Total incorrect")
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
print('-----------------------------------------------------')
print('Vertical Histogram')
print('Progress',progress,'|' 'Trailer',module_trailer,'|' 'Retriever',module_retriever,'|''Exclude',exclude)
for v in range(max(progress,module_trailer,module_retriever,exclude)):
    print('     {0}         {1}           {2}           {3}'.format(
                '*' if v < progress else ' ',
                '*' if v < module_trailer else ' ',
                '*' if v < module_retriever else ' ',
                '*' if v < exclude else ' '))
print(total,'outcomes in total.')
