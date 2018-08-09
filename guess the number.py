
# Guess the number game application
from random import randint
n=randint(1,100)
lis=[]
#print(n)
try:
    g=int(input('Guess the number ?'))
    lis.append(g)
    def warmer_colder(g,lis,diff,cond):
        while(g!=n):
            lis.append(g)
            if(diff>=abs(g-n)and g>1 and g<100):
                #print('why',diff,abs(g-n))
                cond='warmer'
                print(cond)
            elif(diff<=abs(g-n)and g>1 and g<100):
                cond='colder'
                print(cond)
            else:
                print('OUT OF BOUNDS')
                break
            diff=abs(g-n)
            g=int(input('Guess another number ?'))
        else: 
            print('guessed in correctly')
            print('number of guesses:',(len(lis)+1))
         
    if (((g>=(n-10) and g<n) or (g>n and g<=(n+10) )) and ( g>1 and g<100)):
        cond='WARM!'
        print(cond)
        diff=abs(g-n)
        g=int(input('Guess another number ?'))
        warmer_colder(g,lis,diff,cond)
    elif (g<=1 or g>=100):
        print('OUT OF BOUNDS')
    elif((g<=(n-10)  or  g>=(n+10) ) and ( g>1 and g<100)):
        cond='COLD!'
        print(cond)
        diff=abs(g-n)
        g=int(input('Guess another number ?'))
        warmer_colder(g,lis,diff,cond)
        
    else:
        print('guessed it correctly')
        print('number of guesses:',(len(lis)))
except:
    print('Invalid Format,Restart the program')
        

        