<?php
include("conexion.php");
// Acceder a los datos enviados por POST
//$serial = $_POST['serial'];

// Imprimir el valor del serial recibido
//echo "El valor del serial es: " . $serial;

$fecha = $_POST['fecha'];
$hora = $_POST['hora'];
$serial = $_POST['serial'];
$modelo = $_POST['modelo'];
$fabricante = $_POST['fabricante'];
$nom_equipo = $_POST['nom_equipo'];
$processor_model = $_POST['processor_model'];
$formatted_ram_capacity = $_POST['ram'];
$slots = $_POST['slots'];





// Insertar los datos en la base de datos
$sql = "INSERT INTO datos (fecha, hora, serial, modelo, fabricante, nom_equipo, nom_procesador, ram, slot)
        VALUES ('$fecha', '$hora', '$serial', '$modelo', '$fabricante', '$nom_equipo', '$processor_model', '$formatted_ram_capacity', '$slots')";

if ($conn->query($sql) === TRUE) {
  echo "Los datos se insertaron correctamente.";
} else {
  echo "Error al insertar los datos: " . $conn->error;
}


mysqli_close($conn);

echo "Fecha Actual: " . $fecha;
echo "Hora Actual: " . $hora;
echo "Serial: " . $serial;
echo "Modelo: " . $modelo;
echo "Fabricante: " . $fabricante;
echo "Nombre del equipo: " . $nom_equipo;
echo "Procesador: " . $processor_model;
echo "RAM: " . $formatted_ram_capacity;
echo "slots: " . $slots;

?>

