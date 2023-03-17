import requests # Lib para enviar la solicitud al servidor
import platform # Lib para el serial
import os # Lib para el modelo
import datetime # Lib para la fecha y la hora

# Encabeza para la información
print ("Soporte Técnico Integeratic  \n")

# Fecha  y hora actual del registro
fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
print("Fecha :", fecha_actual + " / " + "Hora : ", hora_actual + "\n")


# Procesos para detectar los datos de computador
# Serial
if platform.system() == "Windows":
    c = os.popen("wmic bios get serialnumber").read()
    V_serial = c.split("\n")[2].strip()
    print("Serial: ", V_serial)
# Modelo    
    a = os.popen("wmic csproduct get name").read()
    V_modelo = a.split("\n")[2].strip()
    print("Modelo: ", V_modelo)
else:
    print("Este código solo funciona en sistemas operativos Windows")


# Prueba
# Variables con la información que quieres enviar
# cedula = "721994011"

# URL del formulario de PHP
# url = "https://tuformulario.com/procesar_datos.php"

# Servidor
# url = "https://sys.integratic.com.co/certificado/proceso.php"
# Local
url = "http://localhost/Proyectos_Integratic/Python-PHP-Soporte/proceso.php"


# Datos que quieres enviar
data = {
    "fecha": fecha_actual,
    "hora" : hora_actual,
    "serial": V_serial,
    "modelo": V_modelo
    
}

# Enviar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.text)