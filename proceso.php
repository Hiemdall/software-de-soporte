<?php
include("conexion.php");

$fecha = $_POST['fecha'];
$hora = $_POST['hora'];
$serial = $_POST['serial'];
$modelo = $_POST['modelo'];
$fabricante = $_POST['fabricante'];
$nom_equipo = $_POST['nom_equipo'];
$processor_model = $_POST['processor_model'];
$formatted_ram_capacity = $_POST['ram'];
$slots = $_POST['slots'];
$discos = json_decode($_POST['discos'], true);
                              

// Tabla info
// Insertar los datos en la base de datos
$sql = "INSERT INTO datos (fecha, hora, serial, modelo, fabricante, nom_equipo, nom_procesador, ram, slot)
        VALUES ('$fecha', '$hora', '$serial', '$modelo', '$fabricante', '$nom_equipo', '$processor_model', '$formatted_ram_capacity', '$slots')";

if ($conn->query($sql) === TRUE) {
  echo "";
} else {
  echo "Error al insertar los datos: " . $conn->error;
}


//Tabla disco
// Recorremos la lista de discos e insertamos cada uno en la base de datos
foreach ($discos as $disco) {
  $unidad = mysqli_real_escape_string($conn, $disco['mountpoint']);
  $capacidad = mysqli_real_escape_string($conn, $disco['capacity']);
  
  $sql = "INSERT INTO disco (puntero, capacidad, serial_id) VALUES ('$unidad', '$capacidad', '$serial')";
  if ($conn->query($sql) === TRUE) {
    echo "";
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }
}


mysqli_close($conn);

echo "Datos guardados correctamente";

?>

