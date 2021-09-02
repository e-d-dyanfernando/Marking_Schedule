# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Name: E.D.D. Fernando

# Student UoW ID: w1839054
# Student IIT ID: 20200473
  
# Date: 17th April 2021 

P = int(input('Please enter your credits at pass:='))
D = int(input('Please enter your credit at defer:='))
F = int(input('Please enter your credit at fail:='))

if P==120:
    print('Progression Outcome = Progress')
elif P==100:
    print('Progression Outcome = Progress(module trailer)')
elif P==80 or P==60 or P==40 and D!=0 or P==20 and D>20 or P==0 and D>50:
    print('Progression Outcome = Do not Progress – module retriever')
elif P==40 and F==80 or P==20 and F>70 or P==0 and F>70:
    print('Progression Outcome = Exclude')

