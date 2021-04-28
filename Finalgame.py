class Game(object):
   cnt=False
   cnt1=False
   cnt2=False
   outdatedgod=[]
   outdatedres=[]
   gsw=""
   gsw1=""
   csw=""

   def __init__(self):
        pass

   
   #this function helps in spliting the cards
   def split_cards(self):
            print("--------------------------------------------------------------------------")
            input("lets split the cards between 2 players. ENTER=Roll.")
            
            import random
            deck_of_cards_characters=('Dormin','lukan','Broodan','Borlin','Eiler','markam','ferler','frodin','Groyder','Golin')
            shuffle=random.sample(deck_of_cards_characters,len(deck_of_cards_characters))

            self.player_1_cards=list(shuffle[0:5])
            self.player_2_cards=list(shuffle[5:10])
            print()
            print("Player 1 characters are")
            print("----------------------------------")

            for i in self.player_1_cards:
                print(list(self.player_1_cards).index(i)+1,i)
            print()
            print("Player 2 characters are")
            print("----------------------------------")
            
            for j in self.player_2_cards:
              print(list(self.player_2_cards).index(j)+1,j)
            print()  
   

              
              
    
    #selecting player on the basis of getting highest value on the dice
   def dice(self):
        import random
        self.count1,self.count2=0,0
        print("---------------------------------START THE GAME-------------------------------")
        num1 = input("Player 1:Start rolling the dice. ENTER=Roll")
        num1=random.randint(1,6)
        print(num1)
        num2=input("Player 2:Start rolling the dice. ENTER=Roll. ")
        num2=random.randint(1,6)
        print(num2)
        if(num1==num2):
            
            while(num1==num2):
                
                print("Please try again")
                num1 = input("Player 1:Start rolling the dice. ENTER=Roll.")
                num1=random.randint(1,6)
                print(num1)
                num2=input("Player 2:Start rolling the dice. ENTER=Roll. ")
                num2=random.randint(1,6)

                print(num2)
            num1==num2    
        if(num1>num2):
            print("player 1 has higher value on the dice.Player 1 will play first")
            self.count1=self.count1+1
            self.winner='Player 1'
            #print(self.count1)
            
        if(num2>num1):
            print("player 2 has higher value on the dice.Player 2 will play first") 
            self.count2=self.count2+1
            self.winner='Player 2'
            #print(self.count2)

      #this function displays all the characteristic on the cards with a random value      
   def characterCharacteristics(self):#DEFINES THE CHARACTERISTICS AND THE VALUES
        import random
        self.c1='STRONG'
        
        self.c1_value=random.randrange(100,120)
        print("the value for the characteristics ",self.c1,"is",self.c1_value)
        self.c2='STABILITY'
        self.c2_value=random.randrange(121,140)
        print("the value for the characteristics ",self.c2,"is",self.c2_value)
        self.c3='INTUTIVE'
        self.c3_value=random.randrange(141,160)
        print("the value for the characteristics ",self.c3,"is",self.c3_value)
        self.c4='DETERMINED'
        self.c4_value=random.randrange(161,180)
        print("the value for the characteristics ",self.c4,"is",self.c4_value)

   #this function will help the evaluator to decide if , Player 1 should play next
   def player1(self):
         self.value='Player 1'
         self.value1='Player 2'
         input("player 1 should select the first card from the deck ENTER=Play.")     
         print(self.player_1_cards[0])
         print()   
         print("the charactereristics for Player1 is")
         print()
         self.characterCharacteristics()     
         self.cp=[self.c1,self.c2,self.c3,self.c4]
         self.cp1_holder=[self.c1_value,self.c2_value,self.c3_value,self.c4_value]
         print()
         input("player2 should select the first card from the deck ENTER=Play.")
         print(self.player_2_cards[0])
   #this function will help the evaluator to decide if , Player 2 should play next
   def player2(self):
         self.value='Player 2'
         self.value1='Player 1'
         input("player2 should select the first card from the deck ENTER=Play.")   
         print(self.player_2_cards[0]) 
         print("the characteristics for Player2")
         self.characterCharacteristics()
        
         self.cp=[self.c1,self.c2,self.c3,self.c4]
         self.cp1_holder=[self.c1_value,self.c2_value,self.c3_value,self.c4_value] 
         print()
         input("player1 should select the first card from the deck ENTER=Play.")
         print(self.player_1_cards[0]) 

   #this function helps in getting the value for the challenged characteristics
   def comparision(self):
        print()
        print(self.value,"must challange",self.value1)
        self.characteristics=input("please enter the characteristics you want to challange. STRONG. STABILITY. INTUTIVE. DETERMINED.  ") 
        print()
        #print("the characterisrtic",self.characteristics)    
        self.characterCharacteristics()


        if (self.characteristics==self.c1 ): #characteristics==self.c1.casefold() or
            self.cp2=self.c1_value
            #print(self.cp2)
        elif (self.characteristics==self.c2):#characteristics==self.c2.casefold() or 
             self.cp2=self.c2_value
             #print(self.cp2)
        elif (self.characteristics==self.c3):#characteristics==self.c3.casefold() or
             self.cp2=self.c3_value
             #print(self.cp2)
        elif (self.characteristics==self.c4):#characteristics==self.c4.casefold() or 
             self.cp2=self.c4_value
             #print(self.cp2)
        else: #while loop for giving 3 incorrect trials
             raise ValueError('please input the valid value in CAPITAL Letters and without any special character')
   
   #this function helps in evaluation which player will play the next round.
   def evaluator(self):
       
       for i in self.cp:
                if self.characteristics in  i:
                    indexvalue=self.cp.index(i)
                    self.cp1=self.cp1_holder[indexvalue]

       self.counter1,self.counter2=0,0
       if(self.cp2>self.cp1):
            print(self.cp2,">",self.cp1)
           
            print(self.value1," has won this round")
            self.counter1+=1
            print(self.value1," Points:",self.counter1)
            print(self.value," Points:",self.counter2) 
            self.winner=self.value1
            #self.outdatedDeck()
       if(self.cp1>self.cp2):
            print(self.cp2,"<",self.cp1)
            print(self.value," has won this round")   
            self.counter2+=1
            print(self.value," Points:",self.counter2)
            print(self.value1," Points:",self.counter1)
            self.winner=self.value
       self.outdatedDeck()
       
   #print("The used deck is",self.outdated_deck)
   
   #This function runs for remaining cards, After the first round
   def strategy2(self):
        

      #iteration=3
        self.gamewinner1=[]
        self.outdated1=[]
        iteration1=len(self.player_1_cards)
        iteration2=len(self.player_2_cards)
        print(iteration1,iteration2)
        if(iteration1 < iteration2 or iteration1==iteration2):
            iteration=iteration1
        elif(iteration2 < iteration1 or iteration1==iteration2):
            iteration=iteration2
        
        

        while(iteration>0):

                if(obj.cnt2==False and obj.cnt1==False):
                    self.godspellStrategy()
                elif(self.godspelllosser=='Player 1'):
                    self.godspellStrategy2()
                elif(self.godspelllosser=='Player 2'):
                    self.godspellStrategy2()


                #self.godspellStrategy()
                self.resurrectStrategy()
                #self.resurrect1()

                if( self.winner=='Player 1'):
                    self.player1()                        
                elif( self.winner=='Player 2'):    
                    self.player2()

                self.comparision()
                self.evaluator()
                iteration=iteration-1
                
                self.endesults()
                self.outdated()
            

            
   
      

    #calculates the outdated deck for the deck of cards   
   def outdatedDeck(self):
          self.remove2=(len(self.player_2_cards)+1) % len(self.player_2_cards)
          #print(self.remove2)
          self.removecards2=self.player_2_cards.pop(self.remove2-1)
          #print(self.player_2_cards)
          

          self.remove1=(len(self.player_1_cards)+1) % len(self.player_1_cards)
          #print(self.remove1)
          self.removecards1=self.player_1_cards.pop(self.remove1-1)
          #print(self.player_1_cards)
          self.outdated_deck=[]
          self.outdated_deck.append(self.removecards1)
          self.outdated_deck.append(self.removecards2)
          #print(self.outdated_deck)
          self.stage1=self.removecards1
          self.stage2=self.removecards2

   def outdated(self):

       for j in self.outdated_deck:
             calc1=j
             self.outdated1.append(calc1)
             #print(self.outdated1)


     #this is a helping function for calculating winners at the end of strategy2     
   def endesults(self):
       self.gameWinner=[]
       self.gameWinner.append(self.winner)
       print(self.gameWinner)
          
       for i in self.gameWinner:
             calc=i
             self.gamewinner1.append(calc)
       

   def strategy(self):
      
      
      if(self.winner=='Player 1'):
                self.player1()
                
      elif(self.winner=='Player 2'):
                self.player2()

   def outdatedround1(self):
       self.outdatedround1=self.stage1
       self.outdatedround2=self.stage2
       #print(self.outdatedround1)
      #print(self.outdatedround2)


    #finds out the winner at the end of first round
   def strategy1_evaluator(self):
       self.round1_evaluator=self.winner
       #print("round one evaluator i",self.round1_evaluator)


   def final_outdated(self):
       self.outdated1.append(self.outdatedround1)
       self.outdated1.append(self.outdatedround2)
       self.outdated1.append(obj.outdatedgod)
       self.outdated1.append(obj.outdatedres)
       print(self.outdated1)

       

   #this function finds out the winner at the end of game
   def final_count(self): 
       #print(self.gamewinner1)
       self.gamewinner1.append(self.round1_evaluator)
       self.gamewinner1.append(self.csw)
       self.gamewinner1.append(self.gsw)
       self.gamewinner1.append(self.gsw1)

       print("The Final Results are:")
       finalWinner = {i:self.gamewinner1.count(i) for i in self.gamewinner1}
       print(finalWinner)
   
   def godspellStrategy(self):
           self.godspellwinner=self.winner
           
       
           if(self.godspellwinner=='Player 1'):
             self.round1losser='Player 2'
           elif(self.godspellwinner=='Player 2'):
             self.round1losser='Player 1'
           
           print(self.godspellwinner,"would you like to play godspell with",self.round1losser)
           message='Please Enter if you want to play god spell. ENTER=PLay. or EXIT=exit. '
           self.godspell=input(message)

           if(obj.cnt1 == False):
              self.godspell1()
           elif(obj.cnt1 == True):
                  print("you have already played the spell")
                  pass

   def godspell1(self):
      
      while(self.godspell !='EXIT'):
            
            godSpellcard=input("Please enter the characteristics that you want to challange STRONG. STABILITY. INTUTIVE. DETERMINED.")
            godSpellChar=int(input("Please enter the card number you want to play"))
            #print(godSpellcard)
            #print(godSpellChar)

            if(self.godspellwinner=='Player 1'):
             print(self.player_1_cards[(godSpellChar)-1])
             
            elif(self.godspellwinner=='Player 2'):
             print(self.player_2_cards[godSpellChar-1])
            
            
            self.characterCharacteristics()

            if   (godSpellcard==self.c1 ): #characteristics==self.c1.casefold() or
                    cp3=self.c1_value
                    #print(self.cp2)
            elif (godSpellcard==self.c2):#characteristics==self.c2.casefold() or 
                    cp3=self.c2_value
                    #print(self.cp2)
            elif (godSpellcard==self.c3):#characteristics==self.c3.casefold() or
                    cp3=self.c3_value
                    #print(self.cp2)
            elif (godSpellcard==self.c4):#characteristics==self.c4.casefold() or 
                    cp3=self.c4_value
                    #print(self.cp2)
            else: #while loop for giving 3 incorrect trials
                    raise ValueError('please input the valid value in CAPITAL Letters and without any special character')
            
            print(cp3)
            if(self.round1losser=='Player 1'):
             print(self.player_1_cards[godSpellChar-1])
             
             
            elif(self.round1losser=='Player 2'):
             print(self.player_2_cards[godSpellChar-1])
             self.player_2_cards.pop(godSpellChar-1)
             
            self.characterCharacteristics()

            if   (godSpellcard==self.c1 ): #characteristics==self.c1.casefold() or
                    cp4=self.c1_value
                    #print(self.cp2)
            elif (godSpellcard==self.c2):#characteristics==self.c2.casefold() or 
                    cp4=self.c2_value
                    #print(self.cp2)
            elif (godSpellcard==self.c3):#characteristics==self.c3.casefold() or
                    cp4=self.c3_value
                    #print(self.cp2)
            elif (godSpellcard==self.c4):#characteristics==self.c4.casefold() or 
                    cp4=self.c4_value
                    #print(self.cp2)
            else: #while loop for giving 3 incorrect trials
                    raise ValueError('please input the valid value in CAPITAL Letters and without any special character')

            print(cp4)
            

            if(cp3>cp4):
                print(self.godspellwinner," won")
                self.winner=self.godspellwinner
                self.godspelllosser=self.round1losser
                obj.gsw=self.godspellwinner
                
            else:
                print(self.godspellwinner," won")
                self.winner=self.godspellwinner
                self.godspelllosser=self.round1losser
                obj.gsw=self.godspellwinner
            
            self.player_1_cards.pop(godSpellChar-1)
            self.player_2_cards.pop(godSpellChar-1)
            self.outdatedgod=[]
            obj.outdatedgod.append(self.player_1_cards[godSpellChar-1])
            obj.outdatedgod.append(self.player_2_cards[godSpellChar-1])
            
            obj.cnt1 = True
            self.godspell ='EXIT'


   def godspellStrategy2(self):

           self.godspellwinner=self.godspelllosser
           
       
           if(self.godspellwinner=='Player 1'):
             self.round1losser='Player 2'
           elif(self.godspellwinner=='Player 2'):
             self.round1losser='Player 1'
           
           print(self.godspellwinner,"would you like to play godspell with",self.round1losser)
           message='Please Enter if you want to play god spell. ENTER=PLay. or EXIT=exit. '
           self.godspell2=input(message)

           if(obj.cnt2 == False):
              self.godspell3()
           elif(obj.cnt2 == True):
                  print("you have already played the spell")
                  pass

   def godspell3(self):
      
      while(self.godspell !='EXIT'):
            
            godSpellcard=input("Please enter the characteristics that you want to challange STRONG. STABILITY. INTUTIVE. DETERMINED.")
            print("no of cards with Player 1:",self.player_1_cards,"plaxer 2:",self.player_2_cards)
            godSpellChar=int(input("Please enter the card number you want to play"))
            #print(godSpellcard)
            #print(godSpellChar)

            if(self.godspellwinner=='Player 1'):
             print(self.player_1_cards[(godSpellChar)-1])
             
            elif(self.godspellwinner=='Player 2'):
             print(self.player_2_cards[godSpellChar-1])
            
            
            self.characterCharacteristics()

            if   (godSpellcard==self.c1 ): #characteristics==self.c1.casefold() or
                    cp3=self.c1_value
                    #print(self.cp2)
            elif (godSpellcard==self.c2):#characteristics==self.c2.casefold() or 
                    cp3=self.c2_value
                    #print(self.cp2)
            elif (godSpellcard==self.c3):#characteristics==self.c3.casefold() or
                    cp3=self.c3_value
                    #print(self.cp2)
            elif (godSpellcard==self.c4):#characteristics==self.c4.casefold() or 
                    cp3=self.c4_value
                    #print(self.cp2)
            else: #while loop for giving 3 incorrect trials
                    raise ValueError('please input the valid value in CAPITAL Letters and without any special character')
            
            print(cp3)
            if(self.round1losser=='Player 1'):
             print(self.player_1_cards[godSpellChar-1])
             
             
            elif(self.round1losser=='Player 2'):
             print(self.player_2_cards[godSpellChar-1])
             self.player_2_cards.pop(godSpellChar-1)
             
            self.characterCharacteristics()

            if   (godSpellcard==self.c1 ): #characteristics==self.c1.casefold() or
                    cp4=self.c1_value
                    #print(self.cp2)
            elif (godSpellcard==self.c2):#characteristics==self.c2.casefold() or 
                    cp4=self.c2_value
                    #print(self.cp2)
            elif (godSpellcard==self.c3):#characteristics==self.c3.casefold() or
                    cp4=self.c3_value
                    #print(self.cp2)
            elif (godSpellcard==self.c4):#characteristics==self.c4.casefold() or 
                    cp4=self.c4_value
                    #print(self.cp2)
            else: #while loop for giving 3 incorrect trials
                    raise ValueError('please input the valid value in CAPITAL Letters and without any special character')

            print(cp4)
            

            if(cp3>cp4):
                print(self.godspellwinner," won")
                self.winner=self.godspellwinner
                self.godspelllosser=self.round1losser
                obj.gsw1=self.godspellwinner
            else:
                print(self.godspellwinner," won")
                self.winner=self.godspellwinner
                self.godspelllosser=self.round1losser
                obj.gsw1=self.godspellwinner
            
            self.player_1_cards.pop(godSpellChar-1)
            self.player_2_cards.pop(godSpellChar-1)
            
            self.outdatedgod=[]
            obj.outdatedgod.append(self.player_1_cards[godSpellChar-1])
            obj.outdatedgod.append(self.player_2_cards[godSpellChar-1])
           
            obj.cnt2 == True
            self.godspell ='EXIT'
               
      
   #to be used only after first round and only when one player wishes to play
   def resurrectStrategy(self):
           self.resurrect=""
           self.round1winner=self.winner
           if(self.winner=='Player 1'):
               self.round1losser='Player 2'
           elif(self.winner=='Player 2'):
               self.round1losser='Player 1'


           print(self.winner,"would you like to play reserect spell with",self.round1losser)
           message='Please Enter if you want to play resurrect spell. ENTER=PLay. or EXIT=exit. '
           self.resurrect=input(message)
           
           if(obj.cnt == False):
              self.resurrect1()
           elif(obj.cnt == True):
                  print("you have already played the spell")
                  pass   
       
           
        

   def resurrect1(self):
        
       import random
       
      
       

       while(self.resurrect !='EXIT'):
           
           
           outdate2=[]
           outdate2.append(self.outdatedround1)
           outdate2.append(self.outdatedround2)
           print(outdate2)
           for j in self.outdated1:
             calc1=j
             outdate2.append(calc1)
           #outdate2.append(self.outdated1)
           print(outdate2)          
           shuffle=random.sample(outdate2,len(outdate2))
           print("the number of cards available in the deck are",len(shuffle))
           randomnumber=int(input("choose the random number for the card to be widrawn from outdated deck"))
           print(randomnumber)

           if(self.round1winner=='Player 1'):
                self.player_1_cards.append(shuffle[randomnumber-1])    
               # print(self.player_1_cards)
                resurrectremove1=self.player_1_cards[-1]
                print(resurrectremove1)
                self.player_1_cards.pop(-1)
           else:
                self.player_2_cards.append(shuffle[randomnumber-1])  
                #print(self.player_2_cards)
                resurrectremove1=self.player_2_cards[-1]
                print(resurrectremove1)
                self.player_2_cards.pop(-1)

           resurrectChar=input("Enter the characteristics that you want to challange STRONG. STABILITY. INTUTIVE. DETERMINED.")
           print(resurrectChar)
           self.characterCharacteristics()
           
           if   (resurrectChar==self.c1 ): #characteristics==self.c1.casefold() or
                    cp3=self.c1_value
                    #print(self.cp2)
           elif (resurrectChar==self.c2):#characteristics==self.c2.casefold() or 
                    cp3=self.c2_value
                    #print(self.cp2)
           elif (resurrectChar==self.c3):#characteristics==self.c3.casefold() or
                    cp3=self.c3_value
                    #print(self.cp2)
           elif (resurrectChar==self.c4):#characteristics==self.c4.casefold() or 
                    cp3=self.c4_value
                    #print(self.cp2)
           else: #while loop for giving 3 incorrect trials
                    raise ValueError('please input the valid value in CAPITAL Letters and without any special character')
            
           print(cp3)
           print(self.round1losser,"Proceed Further")
           input("should select the first card from the deck ENTER=Play.")
           if(self.round1winner=='Player 1'):
              print(self.player_2_cards[0])

           else:
              print(self.player_1_cards[0])

           self.characterCharacteristics()

           if   (resurrectChar==self.c1 ): #characteristics==self.c1.casefold() or
                        cp4=self.c1_value
                        #print(self.cp2)
           elif (resurrectChar==self.c2):#characteristics==self.c2.casefold() or 
                        cp4=self.c2_value
                        #print(self.cp2)
           elif (resurrectChar==self.c3):#characteristics==self.c3.casefold() or
                        cp4=self.c3_value
                        #print(self.cp2)
           elif (resurrectChar==self.c4):#characteristics==self.c4.casefold() or 
                        cp4=self.c4_value
                        #print(self.cp2)         
           else: #while loop for giving 3 incorrect trials
                        raise ValueError('please input the valid value in CAPITAL Letters and without any special character')  
            
           print(cp3,cp4)
           if(cp3>cp4):
                print("Player2 won")
                self.winner='Player 2'
                obj.csw='Player 2'
           else:
                print("player1 won")
                self.winner='Player 1'
                obj.csw='Player 2'


           
           if(self.round1winner=='Player 1'):
              obj.outdatedres=self.player_2_cards[0]

           else:
              obj.outdatedres=self.player_1_cards[0]
           
           print(self.outdated1)
           obj.cnt=True
           self.resurrect ='EXIT'
           
           
   


   #final function for calling the other sun functions 
   def game(self):
      
        self.dice()
        self.split_cards()
        self.godspellStrategy()

        self.strategy()
        self.comparision()
        self.evaluator()
        self.strategy1_evaluator()
        
        self.outdatedround1()
       
        self.strategy2()
       
        print(self.gamewinner1)
        self.final_count()
        #self.final_outdated()
   
       


obj=Game()
obj.game()

