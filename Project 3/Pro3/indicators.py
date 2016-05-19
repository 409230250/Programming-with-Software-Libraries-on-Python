##Junjie Lin 25792830, Project3

########################################
##Function of gettting a list of prices:

def get_prices(information):
    '''Input as information is the quotes from downloading quotes.
       Return a list of prices that user wants to use for either
       directional indicator or simple moving average.'''
    prices=[]
    for i in information:
        prices.append(i[4])
    return prices

###################################
## A LIST OF Directional indicator:

def Dir_indicator(prices,n):
    '''The N-day directional indicator for a stock is the number of
       days out of the previous N on which the stock went up minus the
       number of days out of the previous N on which the stock went down.
       Take a list of prices and the N-day
       to make a list of directional indicators(depends on different N).'''

    result=[]
    for i in range(len(prices)):
        total=0
        if n>i:
            j=i
        else:
            j=n
        for a in range(j):
            if prices[a+i-j] > prices[a+i+1-j]:
                total-=1
            elif prices[a+i-j] < prices[a+i+1-j]:
                total+=1

        result.append(total)
    return (result)  

###################################
## A LIST OF SIMPLE MOVING AVERAGE:

def SMA(prices,n):
    '''The N-day simple moving average at the end of a particular day
       is the average of the previous N closing prices.
       Take a list of prices and the N-day
       to make a list of average prices(depends on different N).'''
    average = []
    price = []
    for i in prices:
        price.append(float(i))
        if len(price)<n:
            average.append('')
        elif len(price)>n:
            price.remove(price[0]) 
            average.append('{:.3f}'.format((sum(price)/n)))
        else:
            average.append('{:.3f}'.format((sum(price)/n)))
    return(average)
