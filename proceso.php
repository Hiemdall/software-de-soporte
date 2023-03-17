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



// Insertar los datos en la base de datos
$sql = "INSERT INTO datos (fecha, hora, serial, modelo)
        VALUES ('$fecha', '$hora', '$serial', '$modelo')";

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


?>

