python = {
           'int':'butun son',
           'float':'xaqiyqiy son',
           'for':'loops',
            'if':'boolen',
            'str':'matn',
            'sorted':'alifbo shaklida tartiblash'
         }
for type, values in sorted(python.items()):
 
   print(f"{type}-{values}\n")

#Countries
countries = {
            'amerika':'washington',
            'uzbekistan':'tashkent',
            'qazaqistan':'astana'
            }
print('Dunyo davlatlari:')
for davlat in sorted(countries):
  print(f"{davlat.upper()}")

print('\nDavlat poytaxtlari')
for poytaxt in sorted(countries.values()):
  print(f"{poytaxt.title()}")

country = input('Qaysi davlatni poytaxtini bilishni xoxlaysiz? ').lower()
capital = countries.get(country)
if capital==None:
  print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
  print(f"{country.upper()}ning poytaxti {capital.title()} city")

  #Restoran
menu = {
    'osh':20000,
    'sho\'rva':15000,
    'bifshteks':18000,
    'norin':20000,
    'mastava':12000,
    'lag\'mon':18000,
    'manti':1500,
    'kabob':10000,
    'somsa':12000
  }
print('3 ta taom buturtma bering.')
taomlar=[]
for n in range(3):
   taomlar.append(input(f"{n+1}-taom: ").lower())

for taom in taomlar:
  if taom in menu:
    print(f"  {taom.title()} {menu[taom]} so'm")
  else:
    print(f"Kechirasiz,bizda {taom}yo'q")
