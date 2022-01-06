import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(year, type(year))
print(now, type(now))
date_of_birth = dt.datetime(year=2022, month=1, day=6, hour=4)
print(date_of_birth)