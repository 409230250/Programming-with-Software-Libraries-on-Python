##Junjie Lin 25792830, Project3
import download_quotes
import indicators
import signal_strategies

def main(information):
    
    a_list_of_prices = indicators.get_prices(information)
    print(a_list_of_prices)
    strategies(a_list_of_prices)
    

def strategies(prices):
    '''It is for user to decide either wants to use directional strategies
    or simple moving average strategies. Takes a list of prices and the inputs
    (BUY, SELL, N-day), then put them into two printing report function. If the inputs
    do not avlid, ask user to enter again. '''
    
    stra=input("Please enter ('d':directional strategy or 's':simple moving average strategy):")
    while stra == 'd':
        BUY=(input('Please enter a number for BUY signals are generated whenever '+
                  'the directional indicator passes above:'))
        SELL=(input('Please enter a number for SELL signals are generated '+
                   'whenever the directional indicator passes below:'))
        N=(input('Please enter the number of days for Simple Moving Average: '))

        try:
            BUY=int(BUY)
            SELL=int(SELL)
            N=int(N)
        except:
            print('Not a valid input, please enter input as number.')
            continue
        
        report_of_directional(BUY,SELL,prices,N)
        break
    
    while stra == 's':
        N=input('Please enter the number of days for Simple Moving Average: ')
        try:
            N=int(N)
        except:
            print('Not a valid input. Please enter N-day as a number')
            continue
        
        report_of_SMA(prices,N)
        break
    
    while stra != 'd' and stra != 's':
        print('Invalid. Please try again.')
        strategies(prices)
        break

####################################################################################################
##Print report:
def report_of_directional(buy,sell,prices,n):
    '''Takes a list of prices and the input(BUY, SELL, and N-day) to
       print the report of directional indicator and signal strategies.'''
    
    a_list_of_dir_indicators=indicators.Dir_indicator(prices,n)
    CLASS = signal_strategies.DIRECTIONAL_SIGNAL(buy,sell,prices,n,a_list_of_dir_indicators)
    y = CLASS.dir_signal()
    date_close=[[],[]]
    for b in information:
        date_close[0].append(b[0])
        date_close[1].append(b[4])
##    print('\nSYMBOL: '+s+'\nSTRATEGY: Directional, buy above '
##                          +str(buy)+', sell below '+str(sell))
    print("\nSYMBOL: {}\nSTRATEGY: Directional: {}, buy above {}, sell below {}.".format(s,n,buy,sell))
    print('\n{:10}  {:6}  {:9}  {}'.format('DATE','CLOSE','INDICATOR','SIGNAL'))

    for i in range(len(date_close[0])):
        print('{:10}  {:6}  {:3}         {}'.format(date_close[0][i],
                    date_close[1][i], a_list_of_dir_indicators[i], y[i])) 

def report_of_SMA(prices,n):
    '''Takes the input(a list of prices and N-day) to
       print the report of simple moving average and signal strategies'''
    
    a_list_of_SMAverage=indicators.SMA(prices,n)
    CLASS = signal_strategies.SMA_SIGNAL(prices,n,a_list_of_SMAverage)
    x=CLASS.simple_signal()
    date_close=[[],[]]
    for b in information:
        date_close[0].append(b[0])
        date_close[1].append(b[4])
    print('\nSYMBOL: ' + s + '\nSTRATEGY: Simple Moving Average')
    print('\n{:10}  {:6}  {:9}  {:5}'.format('DATE','CLOSE','INDICATOR','SIGNAL'))

    for i in range(len(date_close[0])):
        print('{:10}  {:6}  {:9}    {:5}'.format(date_close[0][i],
                            date_close[1][i], a_list_of_SMAverage[i], x[i])) 

####################################################################

if __name__=='__main__':
    
    while True:
        s=input('Please enter a symbol such as GOOG: ')
        start_date=input('Please enter start_date as YYYY-MM-DD: ')
        end_date=input('Please enter end_end as YYYY-MM-DD: ')
        try:
            start_date = start_date.split('-')
            a = int(start_date[1])
            b = int(start_date[2])
            c = int(start_date[0])

            end_date = end_date.split('-')
            d = int(end_date[1])
            e = int(end_date[2])
            f = int(end_date[0])
            
            download_quotes.check_date(a,b,c,d,e,f) ##First, check the dates.        
        except:
            print('Not a valid date. Please try again.')    
            continue
        try:
            information=download_quotes.download(s,a,b,c,d,e,f) ## 2nd, check the symbol.
        except:
            print('Not a valid symbol. Please try again.')
            continue
        
        break

    main(information)












