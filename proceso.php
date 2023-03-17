<?php
include("conexion.php");
// Acceder a los datos enviados por POST
//$serial = $_POST['serial'];

// Imprimir el valor del serial recibido
//echo "El valor del serial es: " . $serial;


$cedula = $_POST['serial'];
$modelo = $_POST['modelo'];



// Insertar los datos en la base de datos
$sql = "INSERT INTO datos (serial, modelo)
        VALUES ('$cedula', '$modelo')";

if ($conn->query($sql) === TRUE) {
  echo "Los datos se insertaron correctamente.";
} else {
  echo "Error al insertar los datos: " . $conn->error;
}


mysqli_close($conn);

echo "El valor del serial es: " . $cedula;

?>

