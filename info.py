import requests # Lib para enviar la solicitud al servidor
import json
import platform # Lib para el serial
import os # Lib para el modelo
import datetime # Lib para la fecha y la hora
import subprocess # Lib para el nombre del fabricante y el procesador
import socket # Lib para el nombre del equipo
import psutil # Lib para identificar la RAM
import wmi # Lib para identificar los slot de la RAM

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

# Memoria RAM
def get_ram_space():
    ram = psutil.virtual_memory()
    total = ram.total / (1024 ** 3)
    return total
ram_capacity = get_ram_space()
formatted_ram_capacity = round(ram_capacity, 1)
print("Memoria RAM: {:.2f} GB".format(get_ram_space()))

# Slot de memoria ram
# Crea una instancia del objeto WMI para acceder a la información del hardware
w = wmi.WMI()
# Obtiene el número total de ranuras de memoria RAM
slots = w.Win32_PhysicalMemoryArray()[0].MemoryDevices
# Imprime el número total de ranuras
print("Ranuras de memoria RAM:", slots)


# Disco
# Obtener la información del disco
disks = psutil.disk_partitions()
disk_info = []
print("Discos :")
for disk in disks:
    try:
        disk_usage = psutil.disk_usage(disk.mountpoint)
        total = disk_usage.total / (1024 ** 3)
        disk_info.append({"mountpoint": disk.mountpoint, "capacity": "{:.2f} GB".format(total)})
    except PermissionError:
        # Ignorar errores de permisos y continuar con el siguiente disco
        continue
    
    
# Imprimir los valores de mountpoint y capacity para cada disco
for disk in disk_info:
    print("Unidad:", disk["mountpoint"])
    print("Capacidad:", disk["capacity"])

"""
# Crear una lista de diccionarios que contengan la información de cada disco
disk_list = []
for disk in disk_info:
    disk_data = {"unidad": disk["mountpoint"], "capacidad": disk["capacity"]}
    disk_list.append(disk_data)
"""


disk_list = [{"unidad": "C:", "capacidad": "100GB"}, {"unidad": "D:", "capacidad": "500GB"}]
print(type(disk_list))
for disco in disk_list:
    print(disco['unidad'])
    print(disco['capacidad'])


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
    "processor_model" : processor_model,
    "ram" : formatted_ram_capacity,
    "slots" : slots,
    "discos": disk_list
}

headers = {'Content-Type': 'application/json'}
# Enviar la solicitud POST
response = requests.post(url, data=data)

# Imprimir la respuesta del servidor
print(response.text)