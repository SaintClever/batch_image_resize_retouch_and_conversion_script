from datetime import datetime, date

today = datetime.today()
print(today)

today = datetime.now()
print(today)

today = date.today()
print(today)

today = datetime.today()
print(today.strftime("%H:%M:%S"))