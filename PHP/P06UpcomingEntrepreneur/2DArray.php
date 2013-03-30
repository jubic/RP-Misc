<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $arrEmployees = array(

                                "1" => array(

                                    Name => "Dana",
                                    Title => "Owner",
                                    Salary => "$60,000"

                                    ),

                               "2" => array(

                                    Name => "Matt",
                                    Title => "Manager",
                                    Salary => "$40,000"

                                    ),
            
                               "3" => array(

                                    Name => "Susan",
                                    Title => "Clerk",
                                    Salary => "$30,000"

                                    )
            
                             );
        ?>
        <table border="1">
            <tr><td> </td>
                <td>Name</td>
                <td>Title</td>
                <td>Salary</td>
            </tr>
            <?php

                for ($i = 1; $i <= count($arrEmployees); $i++) {
                    echo "<tr><td>".$i."</td><td>".$arrEmployees[$i]['Name']."</td>
                        <td>".$arrEmployees[$i]['Title']."</td>
                            <td>".$arrEmployees[$i]['Salary']."</td>";
                }

            ?>
        </table>
    </body>
</html>
