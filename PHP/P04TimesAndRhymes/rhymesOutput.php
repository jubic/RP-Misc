<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Rhymes</h1>
        <?php
        $animal1 = $_POST['animal1'];
        $sound1 = $_POST['sound1'];

        $animal2 = $_POST['animal2'];
        $sound2 = $_POST['sound2'];

        $animal3 = $_POST['animal3'];
        $sound3 = $_POST['sound3'];

        $animal1 = strtolower($animal1);
        $sound1 = strtoupper($sound1);
        
        $animal2 = strtolower($animal2);
        $sound2 = strtoupper($sound2);

        $animal3 = strtolower($animal3);
        $sound3 = strtoupper($sound3);

        echo "Old Macdonald had a farm, E-I-E-I-O<br>";
        echo "And on his farm he had a <u>".$animal1."</u>, E-I-E-I-O<br>";
        echo "With a <u>".$sound1."</u>-<u>".$sound1."</u> and a <u>".$sound1."</u>-<u>".$sound1."</u> there<br>";
        echo "Here a <u>".$sound1."</u> there a <u>".$sound1."</u><br>";
        echo "Everywhere a <u>".$sound1."</u>-<u>".$sound1."</u><br>";
        echo "Old Macdonald had a farm, E-I-E-I-O<br><br>";

        echo "Old Macdonald had a farm, E-I-E-I-O<br>";
        echo "And on his farm he had a <u>".$animal2."</u>, E-I-E-I-O<br>";
        echo "With a <u>".$sound2."</u>-<u>".$sound2."</u> and a <u>".$sound2."</u>-<u>".$sound2."</u> there<br>";
        echo "Here a <u>".$sound2."</u> there a <u>".$sound2."</u><br>";
        echo "Everywhere a <u>".$sound2."</u>-<u>".$sound2."</u><br>";
        echo "Old Macdonald had a farm, E-I-E-I-O<br><br>";

        echo "Old Macdonald had a farm, E-I-E-I-O<br>";
        echo "And on his farm he had a <u>".$animal3."</u>, E-I-E-I-O<br>";
        echo "With a <u>".$sound3."</u>-<u>".$sound3."</u> and a <u>".$sound3."</u>-<u>".$sound3."</u> there<br>";
        echo "Here a <u>".$sound3."</u> there a <u>".$sound3."</u><br>";
        echo "Everywhere a <u>".$sound3."</u>-<u>".$sound3."</u><br>";
        echo "Old Macdonald had a farm, E-I-E-I-O";
        ?>
    </body>
</html>
