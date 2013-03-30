<?php
    session_start();
    $memberID = $_POST['userID'];

    if(isset($_SESSION['user_id'])){
        $HOST = 'localhost';
        $USERNAME = 'root';
        $PASSWORD = '';
        $DB = 'c203';

        $link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
        $sql = "UPDATE users SET role = 'Moderator' WHERE user_id = $memberID";
        $result = mysqli_query($link,$sql) or die(mysqli_error($link));
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Boomdosh</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
    <meta http-equiv="refresh" content="1;url=userManagement.php"/>
</body>
</html>