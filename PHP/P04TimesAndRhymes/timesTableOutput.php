<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Times - Multiplication Table</title>
    </head>
    <body>
        <h1>Times - Multiplication Table</h1>
        <?php
        $table = $_POST['table'];
        $max = $_POST['max'];

        if($table>=2&&$table<=8) {
            for($value = 1; $value <= $max; $value++) {
                $result = $table * $value;
                echo $table." x ".$value." = ".$result."<br>";
            }
        }

        else {
            echo "Times Table not in syallabus!<br><br>";
        }
        echo"<br>"
        ?>
    </body>
</html>