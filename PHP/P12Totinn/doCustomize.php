<?php
session_start();
if(isset($_POST))
{
    //retrieve colour selected from form
    $colour = $_POST['bgcolour'];

    //set cookie
    setcookie("colour", $colour, time()+60*60*24*365*10);

    $statusMessage = "Your background colour is changed.<br />";
    $statusMessage .= "<a href='index.php'>Home</a>";
}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <p>
        <?php
            echo $statusMessage;
        ?>
        </p>
    </body>
</html>
