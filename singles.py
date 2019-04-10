import sys
import datetime
import billboard

YEAR    = input("Which year do you want to look up? (leave blank for 1984) : ") or "1984"
CHART   = 'hot-100'
NOW = datetime.datetime.now().strftime("%m-%d")

"""  
String Concatenation
The START_DATE variable has to be properly formatted 
before it is passed into billboard.ChartData()
""" 
START_DATE  = YEAR + '-' + NOW

"""  
Create a Readable/User Friendly Date String
This will be printed out in the result

First, we have to convert our string into a proper date object...
"""  
DATE_OBJECT     = datetime.datetime.strptime(START_DATE, '%Y-%m-%d')
"""
Next, we convert our DATE_OBJECT into a string value that we will interpolate later...
"""
READABLE_DATE   = datetime.datetime.strftime(DATE_OBJECT,'%B %d, %Y')

def number_one_single():
    chart = billboard.ChartData(CHART, date=START_DATE)
    number_one = chart[0]
    """     
    String Interpolation
    %s = string
    %d = integer 
    """
    print ('The #1 single for %s is %s' % (READABLE_DATE, number_one))

def main():
    number_one_single()

if __name__ == '__main__':
    main()