<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>

        <h1>SHOUT me</h1>

        <?php

        // Insert data into database

            $link = mysqli_connect('localhost', 'root', '', 'c203') or die(mysqli_connect_error());

            $insertName = $_POST['name'];
            $insertMSG = $_POST['message'];
            date_default_timezone_set('Asia/Singapore');
            $time = date('Y-n-d H:i:s');

            $insert = "INSERT INTO shoutbox(id,name,message,date_submitted) VALUES (NULL,'$insertName','$insertMSG', '$time')";

            $insertResult = mysqli_query($link, $insert) or die('Error querying database');

        // Grab from database

            $grab = "SELECT * FROM shoutbox ORDER BY 'date_submitted'";

            $grabResult = mysqli_query($link, $grab) or die(mysqli_error($link));

            mysqli_close($link);

             while($row=mysqli_fetch_assoc($grabResult))
            {
                $arrMessages[] = $row;
            }

        ?>
        <table border="1">
            <tr>
                <th colspan="3">SHOUT me</th>
                <th>Total number of messages: <?php echo count($arrMessages); ?></th>
            </tr>


            <tr>
                <th>Name</th>
                <th>Message</th>
                <th>Date</th>
                <td rowspan="11">
                    <form method="POST" action="">

                        <table width="400px" border="0">

                            <tr>

                                <td><label for="name">Name:</label></td>
                                <td><input type="text" id="name" name="name"/></td>

                            </tr>

                            <tr>

                                <td><label for="message">Message:</label></td>
                                <td><textarea id="message" name="message" rows="10" cols="16"></textarea></td>

                            </tr>

                            <tr>

                                <td>&nbsp;</td>
                                <td><input name="submit" value="Submit" type="submit"><input type="reset" value="Reset"></td>

                            </tr>

                        </table>

            </form>
                </td>
            </tr>

            <?php
                for($msgCount=1;$msgCount < count($arrMessages);$msgCount++)
                {
                    $name = $arrMessages[$msgCount]['name'];
                    $msg = $arrMessages[$msgCount]['message'];
                    $date = $arrMessages[$msgCount]['date_submitted'];
                ?>
            
                <tr>
                    <td><?php echo $name; ?></td>
                    <td><?php echo $msg; ?></td>
                    <td><?php echo $date; ?></td>
                </tr>
                
                <?php
                }
                ?>
        </table>
        
    </body>
</html>
