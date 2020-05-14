import random

number = 0
suma = 0
while (number >= 0):
    number = int(input('iveskite skaiciu: '))
    suma += number
    print(suma)
    if (number < 0):
        print('suma yra ' + str(suma))
        break
words = []

for word in range(5):
    words.append(str(input('Isveskite zodi ')));

for word in words:
    ilgis = len(word)
    skaicius = words.index(word)
    print(word + ', zodzio ilgis yra ' + str(ilgis) + ' simboliai. Jo vieta sarase yra: ' + str(skaicius))

for skaiciu in range(3):
    x = random.randint(1, 6)
    print(x)
    if (x == 5):
        print('tu pralaimejai')
        break
    else:
        print('tu laimejai')

years = int(input('Iveskite metus: '))

if (years % 400 == 0) or (years % 4 == 0 and years % 100 != 0):
    print('keliamieji')
else:
    print('nekeliamieji')


years = range(1900, 2024, 4)

for year in years:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, 'keliamieji')
    else:
        print(year, 'nekeliamieji')

