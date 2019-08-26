import calendar

calendarBoard = '''          {35}              
          || Mon || Tue || Wed || Thu || Fri || Sat || Sun ||
            -----  -----  -----  -----  -----  -----  -----  
          ||   {0}||   {1}||   {2}||   {3}||   {4}||   {5}||   {6}|| 
          ||_____||_____||_____||_____||_____||_____||_____||
          ||     ||     ||     ||     ||     ||     ||     ||      
          ||   {7}||   {8}||   {9}||   {10}||   {11}||   {12}||   {13}||
          ||_____||_____||_____||_____||_____||_____||_____||
          ||     ||     ||     ||     ||     ||     ||     ||
          ||   {14}||   {15}||   {16}||   {17}||   {18}||   {19}||   {20}||
          ||_____||_____||_____||_____||_____||_____||_____||
          ||     ||     ||     ||     ||     ||     ||     ||
          ||   {21}||   {22}||   {23}||   {24}||   {25}||   {26}||   {27}||
          ||_____||_____||_____||_____||_____||_____||_____||
          ||     ||     ||     ||     ||     ||     ||     ||
          ||   {28}||   {29}||   {30}||   {31}||   {32}||   {33}||   {34}||
          ||_____||_____||_____||_____||_____||_____||_____||'''


def checkInput():
    while True:
        try:
            month, year = input('Give a month and a year separated with \"/\"').split('/')
            month = int(month)
            year = int(year)
            return month, year
            break
        except ValueError:
            print('Invalid input.Try again')
            continue

def createCalendar(month, year):
    calendarList = calendar.monthcalendar(year, month)
    calendarList = flattenListAndMakeElementsStrings(calendarList)
    return calendarList
def flattenListAndMakeElementsStrings(list):
    newList = []
    for sublist in list:
        for item in sublist:
            if item / 10 == 0:
                newList.append('  ')
            elif item / 10 < 1:
                newList.append(' ' + str(item))
            else:
                newList.append(str(item))
    newList.append(calendar.month_name[month] + ' ' + str(year))
    return newList



calendarDays = []
month, year = checkInput()
calendarDays = createCalendar(month, year)

print(calendarDays)
print(calendarBoard.format(calendarDays[0],calendarDays[1],calendarDays[2],calendarDays[3],calendarDays[4],
calendarDays[5],calendarDays[6],calendarDays[7],calendarDays[8],calendarDays[9],calendarDays[10],
calendarDays[11],calendarDays[12],calendarDays[13],calendarDays[14],calendarDays[15],calendarDays[16],
calendarDays[17],calendarDays[18],calendarDays[19],calendarDays[20],calendarDays[21],calendarDays[22],
calendarDays[23],calendarDays[24],calendarDays[25],calendarDays[26],calendarDays[27],calendarDays[28],
calendarDays[29],calendarDays[30],calendarDays[31],calendarDays[32],calendarDays[33],calendarDays[34],calendarDays[-1]))




