import datetime

file = open('today.txt', 'r')
today_date = file.read()
file.close()

today = datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print('Today is', today)