<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $link = mysqli_connect('localhost', 'root', '', 'c203') or die(mysqli_connect_error());

        $query = "INSERT INTO employees(id,name,dept) VALUES (1236,'Steuart','OHR')";

        $result = mysqli_query($link, $query) or die('Error querying database');

        mysqli_close($link);
        ?>
    </body>
</html>
