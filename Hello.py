temperature = []
with open('D:/Python/txt.txt') as t:
    for line in t: 
        temperature.append(int(line))

print(temperature)

avg = sum(temperature)/len(temperature)

temperature_deviation = []

for t in temperature:
    temperature_deviation.append(t - avg)

print(avg)

with open('D:/Python/average_temperature.txt', 'w') as aver_tem:
    aver_tem.write('%.2f' % avg)

with open('D:/Python/temperature_deviation.txt', 'w') as temp_dev:
    for t in temperature_deviation:
        temp_dev.write('%.2f\n' % t)