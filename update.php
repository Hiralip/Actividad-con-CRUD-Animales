<?php
    //SE CREA LA CONEXION A LA BBDD
    $conexion = mysqli_connect("localhost","id19892893_user_ws","pC[GETzs.&#M7k78","id19892893_web_service");
if (!$conexion){
    echo "Error de conexion";
}
//VARIABLES PARA OBTENER DATOS DE PY
$id = $_POST['idn'];
$nombre = $_POST['nombren'];
$raza = $_POST['razan'];
$tipo = $_POST['tipon'];
$apodo = $_POST['apodon'];
$color = $_POST['colorn'];
$fecha = $_POST['fechan'];
$hora = $_POST['horan'];

//VARAIBLE PARA INSERTAR DATOS
$sql = "UPDATE mascotas SET nombremascotas = '$nombre', raza = '$raza', tipo = '$tipo', apodo = '$apodo', color = '$color', fechanacimiento = '$fecha', horanacimiento = '$hora' WHERE idmascotas='$id'";
$resultado = mysqli_query($conexion,$sql);

if ($resultado){
    echo "Datos actualizados";
}else{
    echo "Error";
}
?>