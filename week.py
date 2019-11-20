from pprint import pprint
cities = {}
with open('D:/Python/week_temperature.txt') as f_week_temperature:
    for city in f_week_temperature:
        temperatures = f_week_temperature.readline()
        cities[city.strip()] = temperatures.split()

for city, temperatures in cities.items():
    avg = 0
    for t in temperatures:
        avg += int(t)
    avg = avg / len(temperatures)
    print(city,'%.2f' % avg)
# pprint(cities)