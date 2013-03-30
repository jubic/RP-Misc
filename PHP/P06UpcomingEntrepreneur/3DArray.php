<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $shop = array(
            
                    array(
                        array("rose", 1.25, 15),
                        array("daisy", 0.75, 25),
                        array("orchid", 1.15, 7)
                        ),

                    array(
                        array("rose", 1.25, 15),
                        array("daisy", 0.75, 25),
                        array("orchid", 1.15, 7)
                        ),

                    array(
                        array("rose", 1.25, 15),
                        array("daisy", 0.75, 25),
                        array("orchid", 1.15, 7)
                        )
            
            );

        echo "<ul>";
        for ( $layer = 0; $layer < 3; $layer++ )
        {
            echo "<li>The layer number $layer";
            echo "<ul>";

            for ( $row = 0; $row < 3; $row++ )
            {
                echo "<li>The row number $row";
                echo "<ul>";

                for ( $col = 0; $col < 3; $col++ )
                {
                    echo "<li>".$shop[$layer][$row][$col]."</li>";
                }
                echo "</ul>";
            echo "</li>";
            }
            echo "</ul>";
            echo "</li>";
        }
        echo "</ul>";
        ?>
    </body>
</html>
