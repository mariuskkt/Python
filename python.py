import random
import datetime
from datetime import timedelta

# Pirma uzduotis
while True:
    try:
        number = int(input('Iveskite skaiciu: '));
        if number > 0:
            teigiamas = True
        else:
            teigiams = False
        break
    except:
        print('Input must be type of integer')

print(teigiamas)
# Pirmos pabaiga

# Antra uzduotis

date = datetime.datetime.now()
print(date)
minus_date = date - timedelta(days=5)
print(minus_date)
plus_hours = date + timedelta(hours=8)
print(plus_hours)

different_date_format = date.strftime("%d %m %Y %I:%M.%S")
print(different_date_format)

# Antros pabaiga

# Trecia uzduotis

while True:
    try:
        d_input = input('Iveskite norima data: (YYYY-MM-DD)')
        date_input_converted = datetime.datetime.strptime(d_input, "%Y-%m-%d")
        date = datetime.datetime.now() - date_input_converted

        print(date)
        break
    except:
        print('blogai ivesta data')

years = date.days // 365
months = date.days // 30
weeks = date.days / 7
days = date.days
hours = date.total_seconds() / 3600
minutes = date.total_seconds() / 60
seconds = date.total_seconds()

print(
    f"{years} metai {months} menesiai {weeks} savaites {days} dienos {hours} valandos {minutes} minutes {seconds} sekundes")

# Trecios pabaiga
