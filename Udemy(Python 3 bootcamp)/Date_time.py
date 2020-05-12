from datetime import *
'''time(hour, minutes, seconds, microseconds, tzinfo) 
   date(year, month, day) '''

t1 = time(5, 40, 15)
print("time -", t1)
print('hour - ',t1.hour)
print('minute - ',t1.minute)
print('sec - ',t1.second)

d1 = date(1999, 6, 21)
print('date:',d1.month)
print('year:',d1.year)
print('month:',d1.month)
print('day:',d1.day)