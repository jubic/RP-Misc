<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $host = "localhost";
        $user = "root";
        $pass = "";
        $db = "c203";

        // open connection
        $link = mysqli_connect($host, $user, $pass, $db);

        // build SQL statement
        $query = "SELECT * FROM employees WHERE name = 'Felicity'";

        // execute SQL statement
        $result = mysqli_query($link, $query) or die(mysqli_error($link));

        mysqli_close($link);

        while ($row=mysqli_fetch_array($result))
        {
        echo $row['id'];
        echo "<br>";
        echo $row['name'];
        echo "<br>";
        echo $row['dept'];
        }
        ?>
    </body>
</html>
