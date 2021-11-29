import pyowm

owm = pyowm.OWM('c4f42a95a4439a6b2f17272281dde468')

place=input('city: ')

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp=w.get_temperature('celsius')['temp']

print('in city the city of '+place+' now '+w.get_detailed_status())
print('temperature is now '+str(temp))

if temp>10:
    print('dress warmer')
elif temp<10:
    print('dress lightly')
else:
    print('dress very warmer')


input()