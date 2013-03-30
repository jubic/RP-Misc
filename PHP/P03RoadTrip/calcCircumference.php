<!--
To change this template, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Quiz</title>
    </head>
    <body>
        <?php
            $radius = $_POST['radius'];
            $pi = 3.142;

            $circumference = (2 * $pi * $radius);

            echo "Radius of circle = ".$radius."<br>";
            echo "Circumference of circle = ".$circumference;
        ?>
    </body>
</html>
