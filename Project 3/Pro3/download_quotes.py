##Junjie Lin 25792830, Project3

import urllib.request

def download(s,a,b,c,d,e,f):
    '''Use the input from interface, which they are symbol and dates,
       and then make a url for downloading quotes from Yahoo Finance.'''
    print('Downloading quotes...')
    a=str(a-1)
    b=str(b)
    c=str(c)
    d=str(d-1)
    e=str(e)
    f=str(f)
    url = 'http://ichart.yahoo.com/table.csv?s=' + s +'&a='+ a + '&b='+ b +'&c=' + c +'&d='+ d +'&e=' + e +'&f=' + f +'&g=d'
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()
    string_data = data.decode(encoding='utf-8')
    print('Downloaded.')
    result=[]
    lines = string_data.splitlines()
    for i in lines:
        a=i.split(',')
        result.append(a)
    result=result[2:]
    result.reverse()
    return (result)

def check_date(a,b,c,d,e,f):
    '''Use the input(dates includes months, days, and yeaars) from interface,
       check them. If they are the valid dates, it pass. If not,
       it raises an error.'''
    if (f==c and d==a and e==b) == True:
        print("Start_date is the same as the end date, so you won't "+
              "download anything and print report will be empty.")
    else:
        pass
    if (1<=a<=12 and 1<=b<=31 and 2004<=c<=2012 and
          1<=d<=12 and 1<=e<=31 and 2004<=f<=2012) == True:
        if (f>=c)==True:
            if (d>=a)==True:
                if (e>=b)==True:
                    print('Input dates are exist.')
                else:
                    print('Error on days(DD), end_date needs to be greater than start_date.')
                    raise Error
            else:
                print('Error on months(MM), end_date needs to be greater than start_date.')
                raise Error
        else:
            print('Error on Years(YYYY), end_date needs to be greater than start_date.')
            raise Error
    else:
        print('Input date is not exist. Please try again.')
        raise Error

                
##check_date(1,1,2012,1,1,2012)
    
