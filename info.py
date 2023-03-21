import requests # Lib para enviar la solicitud al servidor
import platform # Lib para el serial
import os # Lib para el modelo
import datetime # Lib para la fecha y la hora
import subprocess # Lib para el nombre del fabricante y el procesador
import socket # Lib para el nombre del equipo

# Encabeza para la información
print ("Soporte Técnico Integeratic SAS  \n")

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

# Fabricante
result = subprocess.run(['wmic', 'csproduct', 'get', 'vendor'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
fabricante = result.stdout.decode().strip().split("\n")[1]
print("Fabricante: ", fabricante)

# Nombre del equipo
nom_equipo = socket.gethostname()
print("Nombre del Equipo : ", nom_equipo)

# Procesador
result = subprocess.run('wmic cpu get name', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
processor_model = result.stdout.strip().splitlines()[2].decode()
# print(f"Modelo de procesador: {processor_model}")
print("Procesador: ",processor_model)

# Servidor
# url = "https://sys.integratic.com.co/certificado/proceso.php"
# Local
url = "http://localhost/Proyectos_Integratic/Python-PHP-Soporte/proceso.php"


# Datos que quieres enviar
data = {
    "fecha": fecha_actual,
    "hora" : hora_actual,
    "serial": V_serial,
    "modelo": V_modelo,
    "fabricante": fabricante,
    "nom_equipo" : nom_equipo,
    "processor_model" : processor_model
}

# Enviar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.text)