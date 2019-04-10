import sys
import datetime
import billboard

PLAYLIST_NAME = '#1 Singles for 1984'
CHART         = 'hot-100'
NOW           = datetime.datetime.now()
START_DATE    = NOW.strftime("1984-%m-%d")

def number_one_single():
    chart = billboard.ChartData(CHART, date=START_DATE)
    number_one = chart[0]
    print (number_one)

def main():
    number_one_single()

if __name__ == '__main__':
    main()