<?php
    //SE CREA LA CONEXION A LA BBDD
    $conexion = mysqli_connect("localhost","id19892893_user_ws","pC[GETzs.&#M7k78","id19892893_web_service");
if (!$conexion){
    echo "Error de conexion";
}
//VARIABLES PARA OBTENER DATOS DE PY
$id = $_POST['idn'];

//VARIABLE PARA ELIMINAR
$sql = "DELETE FROM mascotas WHERE idmascotas = '$id'";
$resultado = mysqli_query($conexion,$sql);

if ($resultado){
    echo "Datos ingresados";
}else{
    echo "Error";
}
?>