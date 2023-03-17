import requests # Lib para enviar la solicitud al servidor
import platform # Lib para el serial
import os # Lib para el modelo


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
url = "http://localhost/Python-PHP-Soporte/proceso.php"

# Datos que quieres enviar
data = {
    "serial": V_serial,
    "modelo": V_modelo
}

# Enviar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.text)