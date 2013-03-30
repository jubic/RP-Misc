<?php
    session_start();
    $memberID = $_POST['userID'];

    if(isset($_SESSION['user_id'])){
        $HOST = 'localhost';
        $USERNAME = 'root';
        $PASSWORD = '';
        $DB = 'c203';

        $link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
        $sql = "UPDATE users SET role = 'Member' WHERE user_id = $memberID";
        $result = mysqli_query($link,$sql) or die(mysqli_error($link));
    }
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Boomdosh</title>
    </head>
    <body>
        <meta http-equiv="refresh" content="1;url=userManagement.php"/>
    </body>
</html>
