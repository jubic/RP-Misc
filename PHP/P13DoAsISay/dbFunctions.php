<?php
$HOST = 'localhost';
$USERNAME = 'root';//letter s followed by your student ID
$PASSWORD = '';//password you used to login
$DB = 'c203';

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
// Function to purify strings
function clean($string) {

    $string = trim($string); // This function returns a string with whitespace stripped from the beginning and end of str. Without the second parameter, trim() will strip these characters
    $string = htmlentities($string, ENT_COMPAT); // This function is identical to htmlspecialchars() in all ways, except with htmlentities(), all characters which have HTML character entity equivalents are translated into these entities.
    $string = addslashes($string); // Returns a string with backslashes before characters that need to be quoted in database queries etc. These characters are single quote ('), double quote ("), backslash (\) and NUL (the NULL byte).
    $string = mysqli_real_escape_string($GLOBALS['link'], $string);

    return $string;

}
?>