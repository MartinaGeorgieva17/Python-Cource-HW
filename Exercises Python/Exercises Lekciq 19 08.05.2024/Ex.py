# Програма за час и дата: 
# Date and time:


# 1..............
# import time - системно време

# now = time.time()
# print(now)



# 2..........................
# Модул datetime.date - човешки формат 
# Клас: datetime........................



# import datetime

# now = datetime.datetime.now()
# print(now)



# 3. Като задача .............


# class A:
#     def __init__(self, id):
#         self.id = id

#     def __str__(self) -> str:
#         return f'id = {self.id}'

# now = A(1)
# print(now)



# 4.Пример: .........................

# import datetime

# now = datetime.datetime.now()
# print(type(now))

# year = now.year
# month = now.month


# print('Year:', year)
# print('Month:', month)





# 5.Как да постигнем: 'DD.MM.YYYY' (08.05.2024)...........................

# import datetime

# now = datetime.datetime.now()
# formated_now_string = now.strftime('%d.%m.%Y')
# print(formated_now_string)





# 6.................................
# Task: calculate user age, given his birthdate?
# ..................................

# import datetime

# birthday = '08.05.1990'

# now = datetime.datetime.now()
# curretn_year = now.year
# print(current_year)


# Как да вземем самата година от задачата 

# import datetime

# birthday_string = '08.05.1990'
# birthdate = datetime.datetime.strptime(birthday_string, '%d.%m.%Y')


# curretn_year = datetime.datetime.now().year
# print(f'User age is: {curretn_year - birthdate.year}')





# 7. timedelta....................................
# Разликата от датата до днешни дни в дни 
# import datetime

# birthdate = datetime.datetime.strptime('08.05.1990', '%d.%m.%Y')
# now = datetime.datetime.now()
# td = now - birthdate
# print(type(td))
# print(td.days)




# 8....................
# Създаваме обект, ние го конструираме, подаваме като отделни обекти


# import datetime

# birthdate_string = '08.05.1990'
# birthdate = datetime.datetime(year=1990,month=5, day = 8)
# print(birthdate)

# birthdate = datetime.datetime.strptime('08.05.1990', '%d.%m.%Y')
# now = datetime.datetime.now()
# td = now - birthdate
# print(type(td))
# print(td.days)




# 9. dateutil............................
# Инсталираме го .............................
# ......Инсталиран е вече!


# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# date1 = datetime(year=2000, month=1, day=30)
# date2 = datetime(year=2010, month=5, day=30)

# date_difference = relativedelta(date2, date1)
# print(date_difference)


# print(date_difference.years)
# print(date_difference.months)
# print(date_difference.days)





# 10. pytz example ...........................
# from datetime import datetime 
# import pytz

# current = datetime.now()
# tz_NY = pytz.timezone('America/New_York')
# tz_London = pytz.timezone('Europe/London')

# current_NY = current.astimezone(tz_NY)
# current_London = current.astimezone(tz_London)

# print("Local time:", current.strftime('%H:%M:%S'))
# print("NY time:", current_NY.strftime('%H:%M:%S'))
# print("London time:", current_London.strftime('%H:%M:%S'))



# 11..........Task: Show time in London for 09.05.2024, 12:00:00 BG time 


# from datetime import datetime 
# import pytz

# tz_London = pytz.timezone('Europe/London')
# given_datetime = datetime(2024, 5, 9, 12, 0, 0, tzinfo=tz_London)
# print(given_datetime)





# 12.........................

# from datetime import datetime 
# import pytz

# tz_London = pytz.timezone('Europe/London')
# tz_Sofia = pytz.timezone('Europe/Sofia')

# sofia_datetime = datetime(2024, 5, 9, 12, 0, 0, tzinfo=tz_London)
# print("Sofia time:", sofia_datetime)

# london_datetime = sofia_datetime.astimezone(tz_London)
# print("London time:", london_datetime)





# 13..................
# # Task: print today day as weekday name 

# from datetime import datetime 

# now = datetime.now()
# print(now.strftime('%A'))




# 14..............................
# # Task: print today day as weekday name - като цифра(отговор)

# from datetime import datetime 

# now = datetime.now()
# print(now.weekday())



# 15...........................

