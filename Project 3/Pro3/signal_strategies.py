##Junjie Lin 25792830, Project3

class DIRECTIONAL_SIGNAL:
    def __init__(self,buy,sell,prices,n,indicator):
        self.b=buy
        self.s=sell
        self.p=prices
        self.n=n
        self.i=indicator
    
    def dir_signal(self):
        '''Buy whenever the N-day directional indicator moves above a chosen
           value; sell whenever it moves below another chosen value.
           The user chooses N (i.e., the number of days)
           and the buy and sell trigger values.'''
        result=[]
        s=''
        for i in self.i:
            if i>self.b:
                if 'BUY' not in result:
                    s='BUY'
                else:
                    temp= []
                    temp.extend(result)
                    while temp[-1] == '':
                        temp.remove(temp[-1])
                    if temp[-1] == 'BUY':
                        s=''
                    else:
                        s='BUY'
            elif i<self.s:
                if 'SELL' not in result:
                    s='SELL'
                else:
                    temp = []
                    temp.extend(result)
                    while temp[-1] == '':
                        temp.remove(temp[-1])
                    if temp[-1] == 'SELL':
                        s=''
                    else:
                        s='SELL'
            else:
                s=''
            result.append(s)
        return (result)

#############################################
##SIGNAL STRAGEIES FOR SIMPLE MOVING AVERGAE:
class SMA_SIGNAL:
    def __init__(self,price,n,average):
        self.p=price
        self.n=n
        self.a=average
    
    def simple_signal(self):
        '''Buy whenever the price moves above the N-day simple moving average;
           sell whenever the price moves below it.
           The user chooses N (i.e., the number of days),
           with a smaller number of days being more sensitive
           and a large number of days being less so.'''
        result=[]
        s=''
        for i in range(len(self.p)):
            if self.a[i] < self.p[i]:
                
                if self.a[i] == '':
                    s=''  
                elif 'BUY' not in result:
                    s='BUY'
                else:
                    temp= []
                    temp.extend(result)
                    while temp[-1] == '':
                        temp.remove(temp[-1])
                    if temp[-1] == 'BUY':
                        s=''
                    else:
                        s='BUY'
                        
            elif self.a[i] > self.p[i]:
                
                if self.a[i] == '':
                    s=''
                elif 'SELL' not in result:
                    s='SELL'
                else:
                    temp = []
                    temp.extend(result)
                    while temp[-1] == '':
                        temp.remove(temp[-1])
                    if temp[-1] == 'SELL':
                        s=''
                    else:
                        s='SELL'
                        
            else:
                s=''
            result.append(s)
        return(result)









