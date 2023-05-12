import time
import winsound

segundos = int(input('Quantos segundos deseja esperar? '))

for i in range(segundos):
    print(segundos)
    segundos = segundos - 1
    time.sleep(1)

if segundos == 0:
    print("\nFIM ! \n")
    frequency = 2500  # Frequência do som em Hz
    duration = 1000   # Duração do som em ms (1 segundo)
    winsound.Beep(frequency, duration)



