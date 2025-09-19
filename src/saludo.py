from datetime import datetime
hora_actual = datetime.now().hour

nombre = input("Introduzca su nombre:")
if hora_actual < 12:
    print(f"¡Buenos dias, {nombre}!")
elif hora_actual > 12 and hora_actual < 20:
    print(f"¡Buenos tardes, {nombre}!")
elif hora_actual > 21 and hora_actual < 23:
    print(f"¡Buenas noches, {nombre}!")
else:
    print("Ha habido un problema")