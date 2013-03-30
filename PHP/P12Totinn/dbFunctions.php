<?php
$HOST = 'localhost';
$USERNAME = 's92807';
$PASSWORD = 'e5d5e4d7';
$DB = 's92807';

$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB) or die(mysqli_connect_error());

function executeSelectQuery($query)
{
    $result = mysqli_query($GLOBALS['link'], $query) or die(mysqli_error($GLOBALS['link']));
    while($row=mysqli_fetch_array($result))
    {
        $returnArray[] = $row;
    }
    return $returnArray;
}
function executeInsertQuery($query)
{
    return mysqli_query($GLOBALS['link'], $query) or die(mysqli_error($GLOBALS['link']));
}
function executeUpdateQuery($query)
{
    return mysqli_query($GLOBALS['link'], $query) or die(mysqli_error($GLOBALS['link']));
}
function createRandomPassword() {
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz0123456789";
    $i = 0;
    $pass = '' ;

    while ($i <= 8) {
        $num = mt_rand(0,58);
        $tmp = substr($chars, $num, 1);
        $pass = $pass . $tmp;
        $i++;
    }
    return $pass;
}
?>
