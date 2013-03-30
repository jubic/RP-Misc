<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        //You can either can the init value of $i in the for loop to 7
        //Or add another condition into the if loop using && ($i>7)
        //Both works the same
        for ($i = 0; $i <= 50; $i++) {
            if ($i%2==0&&$i>7) {
                echo $i."<br>";
            }
        }
        ?>
    </body>
</html>
