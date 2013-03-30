<!DOCTYPE HTML>
<?php
$COST = 100;
$PRICE = 80;

for ($QUANTITY = 1; $QUANTITY <= 10; $QUANTITY++) {
    
    $price = $QUANTITY * $COST;
    $DPRICE = $PRICE * $QUANTITY;
    $save = $price-$DPRICE;
    $tempArr = array($QUANTITY, $price,$DPRICE,$save);
    $arrPrice[] = $tempArr;

}
?>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>P06 - Upcoming Entrepreneur</title>
    </head>
    <body>

        <table border="1" width="700">

            <tr><th colspan="6">Product Information</th></tr>

            <tr>

                <td rowspan="7"><img src="shoe.png" alt="shoe.png"></td>
                <td><b>Model Name:</b></td>
                <td colspan="4">Nike Skeet</td>

            </tr>

            <tr>

                <td><b>Available Colors:</b></td>

                <td colspan="4">

                    <ul>

                        <li>Black/Black</li>
                        <li>Black/White</li>
                        <li>Black/White-Varsity Red</li>
                        <li>Mid Fog/Photo Blue-White-Black</li>
                        <li>Midnight Fog/White-Black-Photo Blue</li>

                    </ul>

                </td>

            </tr>

            <td rowspan="5"><b>Available Sizes:</b></td>

                <tr>

                    <td><center>6</center></td>
                    <td><center>6.5</center></td>
                    <td><center>7</center></td>
                    <td><center>7.5</center></td>

                </tr>

                <tr>

                    <td><center>8</center></td>
                    <td><center>8.5</center></td>
                    <td><center>9</center></td>
                    <td><center>9.5</center></td>

                </tr>

                <tr>

                    <td><center>10</center></td>
                    <td><center>10.5</center></td>
                    <td><center>11</center></td>
                    <td><center>11.5</center></td>

                </tr>

                <tr>

                    <td><center>12</center></td>
                    <td><center>12.5</center></td>
                    <td><center>13</center></td>
                    <td><center>14</center></td>

                </tr>
            
        </table>

        <br>

        <table border="1" width="700">

            <tr>

                <th>Quantity</th>
                <th>Usual Price</th>
                <th>Discounted Price</th>
                <th>You Save</th>

            </tr>
            
        <?php

            for ($shoescount = 0; $shoescount < count($arrPrice); $shoescount++) {
            $numshoes = $arrPrice[$shoescount][0];
            $price = $arrPrice[$shoescount][1];
            $discounted=$arrPrice[$shoescount][2];
            $savings=$arrPrice[$shoescount][3];

        ?>

        <tr>

            <td><?php echo "<center>$numshoes</center>";?></td>
            <td><?php echo "<center>$price</center>";?></td>
            <td><?php echo "<center>$discounted</center>";?></td>
            <td><?php echo "<center>$savings</center>";?></td>

        <tr>

        <?php

            }
        ?>

        </table>

    </body>

</html>