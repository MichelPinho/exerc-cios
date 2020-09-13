x = int(input(' Digite a medida em Metros (M): '))
dec = x / 10
cen = x / 100
mil = x / 1000
dam = x * 10
hek = x * 100
km = x * 1000

print(f' As medidas convertidas são :\n {km} Km \n {hek} Hek\n {dam} Dec\n {x} M \n {dec} Dec \n {cen} Cen \n {mil} Mil')
