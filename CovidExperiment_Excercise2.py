
groupsize=5
def batch(popsize,groupsize):
    #   i=0;
    #   while i in range(0,len(popsize),groupsize):
    #       yield popsize[i:i + groupsize]


    for i in range(0,len(popsize),groupsize):
        yield popsize[i:i + groupsize] 


listformation=list(batch(list(range(0,13)),groupsize))
#below  is to check  the equal groupsize
lenthoflastgroup=len(listformation[-1])


if(lenthoflastgroup < groupsize):
    print("the size of last group is not equal to group size that is",lenthoflastgroup,"hence removing")
    listformation.pop() #removes the last list from the array
    import random
for k in listformation:
      #print(len(k))
   import random   
   randomnum=random.choice(k)
   import datetime
   print("The random participant for corona test from group",listformation.index(k)+1, "is",randomnum,"participant",datetime.datetime.now())
   
    