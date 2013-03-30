<?php
$host = 'localhost';
$username = 'root';
$password = '';
$db = 'c203';
$link = mysqli_connect($host,$username,$password,$db);

// create query
$query = "SELECT * FROM employees";

// execute query
$result = mysqli_query($link, $query);

while($row=mysqli_fetch_assoc($result))
{
    $arrEmployees[] = $row;
}

//debugging purpose
print_r($arrEmployees);
?><br/><br/>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Department</th>
            </tr>
        <?php
        for($empCount=0;$empCount < count($arrEmployees);$empCount++)
        {
            $id = $arrEmployees[$empCount]['id'];
            $name = $arrEmployees[$empCount]['name'];
            $dept = $arrEmployees[$empCount]['dept'];
        ?>
            <tr>
                <td><?php echo $id; ?></td>
                <td><?php echo $name; ?></td>
                <td><?php echo $dept; ?></td>
            </tr>
        <?php
        }
        ?>
        </table>
    </body>
</html>
