import datetime
import os

# d = datetime.date(2016,7,24)
# tday = datetime.date.today() 
# t = datetime.time()

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

# print(tday.year)
# print(tday.weekday())
# print(tday.isoweekday())
# tdelta = datetime.timedelta(days=7)
# print (tday + tdelta)
# print(dt_now)
# print(dt_utcnow)

print(dt_today)
print(dt_today.hour)

print(dir(os))
