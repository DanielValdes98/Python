#pip install pytz -> Para trabajar con zonas horarios del mundo


from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)

# Se debe correr en el CMD, sino no funciona por el entorno virtual creado
print("Bogota: ", bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)

# Se debe correr en el CMD, sino no funciona por el entorno virtual creado
print("Ciudad de mexico: ", mexico_date.strftime('%d/%m/%Y, %H:%M:%S'))




