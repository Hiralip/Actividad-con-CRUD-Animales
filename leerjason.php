<?php

//FUNCION PARA CONECTAR BBDD
function connectDB(){
    $conexion = mysqli_connect("localhost","id19892893_user_ws","pC[GETzs.&#M7k78","id19892893_web_service");
    return $conexion;
}

//FUNCION PARA DESCONECTAR BBDD
function disconnectDB($conexion){
    $close = mysqli_close($conexion);
    return $close;
}

//VARIABLE PARA SELECCIONAR DE LA BBDD
$sql="SELECT * FROM mascotas";

echo json_encode(getArraysql($sql)); //TRANSFORMA EN JSON LA VARIABLE SQL

function getArraysql($sql){
    $conexion = connectDB();
    mysqli_set_charset($conexion,"utf8");
    if(!$result = mysqli_query($conexion,$sql)) die(); //si la conexion existe cancelalo

    $rawdata=array(); // Si funciona crear arreglo
    $i = 0;
    while($row = mysqli_fetch_array($result))
    {
        $rawdata[$i] = $row;
        $i++;
    }
    disconnectDB($conexion);
    return $rawdata;
}
?>
