

class Apalara:
    row1=[0, 0, 0, 0, 0, 0, 1, 2, 3]
    
    input=0
    box1=0
    box2=0
    box3=0
    position=0
    holder1=0
    holder2=0
def GameStart(self):
    print (self.row1[0:3])
    print (self.row1[3:6])
    print (self.row1[6:9])
    while(True):
       GameOption(Apalara)
       if(self.input==5):
           SystemExit
    
def GameOption(self):
    print ("Press 1 key to Swap any 2 boxes")
    print ("Press 2 key to place a box under another box")
    print ("Press 3 key to place a box on top another box")
    print ("Press 4 key to exit")
    self.input=input()
    
    if(self.input==1):
        GameSwap(Apalara)
    elif(self.input==2):
        GameUnder(Apalara)
    elif(self.input==3):
        GameTop(Apalara)
    elif(self.input==4):
        Gameend(Apalara)

def GameSwap(self):
    z1=0
    z2=0
    print ("Enter the boxes to swap")
    self.box1=input()
    print ("and?")
    self.box2=input()
    if((self.box1==1)&(self.box2==2)|(self.box1==2)&(self.box2==1)):
        print ("Checking")
        if(CheckingClear1(Apalara)&CheckingClear2(Apalara)):
            i=0
            print ("clear")
            while(True):
                i=i+1
                self.holder1=self.row1[i]
                z1=i
                if(self.row1[i]==1):
                    print (self.holder1)
                    break;
            i=0
            while(True):
                i=i+1
                self.holder2=self.row1[i]
                z2=i
                if(self.row1[i]==2):
                    print (self.holder2)
                    break;
            
            self.row1[z1]=self.holder2
            self.row1[z2]=self.holder1
                
        else:
            print ("Not Swappabless")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==1)&(self.box2==3)|(self.box1==3)&(self.box2==1)):
        if(CheckingClear1(Apalara)&CheckingClear3(Apalara)):
            i=0
            print ("clear")
            while(True):
                i=i+1
                self.holder1=self.row1[i]
                z1=i
                if(self.row1[i]==1):
                    print (self.holder1)
                    break;
            i=0
            while(True):
                i=i+1
                self.holder2=self.row1[i]
                z2=i
                if(self.row1[i]==3):
                    print (self.holder2)
                    break;
            
            self.row1[z1]=self.holder2
            self.row1[z2]=self.holder1
        else:
            print ("Not Swappabless")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9]) 
    elif((self.box1==2)&(self.box2==3)|(self.box1==3)&(self.box2==2)):
        if(CheckingClear2(Apalara)&CheckingClear3(Apalara)):
            i=0
            print ("clear")
            while(True):
                i=i+1
                self.holder1=self.row1[i]
                z1=i
                if(self.row1[i]==2):
                    print (self.holder1)
                    break;
            i=0
            while(True):
                i=i+1
                self.holder2=self.row1[i]
                z2=i
                if(self.row1[i]==3):
                    print (self.holder2)
                    break;
            
            self.row1[z1]=self.holder2
            self.row1[z2]=self.holder1
        else:
            print ("Not Swappabless")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9]) 
def CheckingClear1(self):
    i=0
    while(True):
           i=i+1
           self.position=i
           if(self.row1[i]==1):
               break
    if(self.position>3):
        self.position=self.position-3
        if(self.row1[self.position]>=1):
            return False
        else:
            return True
    else:
        return True
def CheckingClear2(self):
   i=0
   while(True):
           i=i+1
           self.position=i
           if(self.row1[i]==2):
               break
   if(self.position>3):
        self.position=self.position-3
        if(self.row1[self.position]>=1):
            return False
        else:
            return True
   else:
        return True
def CheckingClear3(self):
    i=0
    while(True):
           i=i+1
           self.position=i
           if(self.row1[i]==3):
               break
    if(self.position>3):
        self.position=self.position-3
        if(self.row1[self.position]>=1):
            return False
        else:
            return True
    else:
        return True

def GameUnder(self):
    z1=0
    z2=0
    print ("Enter the boxes to place under the other")
    self.box1=input()
    print ("under?")
    self.box2=input()
    if((self.box1==1)&(self.box2==2)):
        if(CheckingClear1(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==2):
                   break;
            if(CheckingClear2(Apalara)):
               print ("clear") 
               
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==3):
                        self.row1[z2-3]=self.holder2
                        break;
            self.row1[z1-3]=self.holder1
            
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==1):
                    self.row1[z1]=1
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==2)&(self.box2==1)):
        if(CheckingClear2(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==1):
                   z1=z1-3 
                   
                   break;
            if(CheckingClear1(Apalara)):
               print ("clear") 
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==3):
                        z2=z2-3
                        self.row1[z2]=self.holder2
                        break;
            self.row1[z1]=self.holder1
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==2):
                    self.row1[z1+3]=2
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==1)&(self.box2==3)):
        if(CheckingClear1(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==3):
                   z1=z1-3 

                   break;
            if(CheckingClear3(Apalara)):
               print ("clear")
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==2):
                        z2=z2-3
                        self.row1[z2]=self.holder2
                        break;
            self.row1[z1]=self.holder1
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==1):
                    self.row1[z1+3]=1
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==3)&(self.box2==1)):
        if(CheckingClear3(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==1):
                   z1=z1-3 
                   
                   break;
            if(CheckingClear1(Apalara)):
               print ("clear") 
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==2):
                        z2=z2-3
                        self.row1[z2]=self.holder2
                        break;
            self.row1[z1]=self.holder1
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==3):
                    self.row1[z1+3]=3
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==2)&(self.box2==3)):
        if(CheckingClear2(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==3):
                   z1=z1-3 
                   
                   break;
            if(CheckingClear1(Apalara)):
               print ("clear") 
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==1):
                        z2=z2-3
                        self.row1[z2]=self.holder2
                        break;
            self.row1[z1]=self.holder1
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==2):
                    self.row1[z1+3]=2
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==3)&(self.box2==2)):
        if(CheckingClear3(Apalara)):
            i=0
            while(True):
                i=i+1
                z1=i
                self.holder1=self.row1[i]
                if(self.row1[i]==2):
                   z1=z1-3 
                   
                   break;
            if(CheckingClear1(Apalara)):
               print ("clear")
            else:
                i=0
                while(True):
                    i=i+1
                    z2=i
                    self.holder2=self.row1[i]
                    if(self.row1[i]==1):
                        z2=z2-3
                        self.row1[z2]=self.holder2
                        break;
            self.row1[z1]=self.holder1
            i=0
            while(True):
                i=i+1
                z2=i
                self.holder1=self.row1[i]
                if(self.row1[i]==3):
                    self.row1[z1+3]=3
                    self.row1[z2]=0
                    break;
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
def GameTop(self):
    l=0
    z1=0
    print ("Enter the boxes to place ONTOP the other")
    self.box1=input()
    print ("ON TOP?")
    self.box2=input()
    if((self.box1==1)&(self.box2==2)):
        if((CheckingClear1(Apalara))&(CheckingClear2(Apalara))):
            i=0
            while(True):
                k=0
                z1=i   
                if(self.row1[i]==2):
                    self.row1[z1-3]=1
                    k=z1-3
                    if(i<8):
                        i=i+1
                if(self.row1[i]==1):
                    l=i
                if((self.row1[l]==1)&(self.row1[k]==1)):
                    print ("debug")
                    self.row1[l]=0
                    break
                if(i<8):
                        i=i+1
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==2)&(self.box2==1)):
        if((CheckingClear1(Apalara))&(CheckingClear2(Apalara))):
            i=0
            while(True):
                k=0
                
                z1=i   
                if(self.row1[i]==1):
                    print ("printing")
                    self.row1[z1-3]=2
                    k=z1-3
                    if(i<8):
                        i=i+1
                if(self.row1[i]==2):
                    print ("printing1")
                    l=i
                
                if((self.row1[l]==2)&(self.row1[k]==2)):
                    self.row1[l]=0
                    print ("printing2")
                    break
                if(i<8):
                        i=i+1
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==1)&(self.box2==3)):
        if((CheckingClear1(Apalara))&(CheckingClear3(Apalara))):
            i=0
            while(True):
                k=0
                
                z1=i   
                if(self.row1[i]==3):
                    self.row1[z1-3]=1
                    k=z1-3
                    if(i<8):
                        i=i+1
                if(self.row1[i]==1):
                    l=i
                if((self.row1[l]==1)&(self.row1[k]==1)):
                    self.row1[l]=0
                    break
                if(i<8):
                        i=i+1
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==3)&(self.box2==1)):
        if((CheckingClear1(Apalara))&(CheckingClear3(Apalara))):
            i=0
            
            while(True):
                k=0
                
                z1=i
                
                if(self.row1[i]==1):
                    
                    self.row1[z1-3]=3
                    print (i)
                    k=z1-3
                    if(i<8):
                        i=i+1
                        
                if(self.row1[i]==3):
                    l=i
                    
                if((self.row1[i]==3)&(self.row1[k]==3)):
                    print ("see3")
                    self.row1[l]=0
                    break
                if(i<8):
                        i=i+1
                        print (self.row1[i])
                        
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==2)&(self.box2==3)):
        if((CheckingClear2(Apalara))&(CheckingClear3(Apalara))):
            i=0
            while(True):
                k=0
                
                z1=i   
                if(self.row1[i]==3):
                    self.row1[z1-3]=2
                    k=z1-3
                    if(i<8):
                        i=i+1
                if(self.row1[i]==2):
                    l=i
                
                if((self.row1[l]==2)&(self.row1[k]==2)):
                    self.row1[l]=0
                    break
                if(i<8):
                        i=i+1
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
    elif((self.box1==3)&(self.box2==2)):
        if((CheckingClear3(Apalara))&(CheckingClear2(Apalara))):
            i=0
            while(True):
                k=0
                
                z1=i   
                if(self.row1[i]==2):
                    self.row1[z1-3]=3
                    k=z1-3
                    if(i<8):
                        i=i+1
                if(self.row1[i]==3):
                    l=i
                    
                if((self.row1[l]==3)&(self.row1[k]==3)):
                    self.row1[l]=0
                    break
                if(i<8):
                        i=i+1
        else:
            print ("Not Movable")
        print (self.row1[0:3])
        print (self.row1[3:6])
        print (self.row1[6:9])
def Gameend(self):
    exit()       
GameStart(Apalara)

