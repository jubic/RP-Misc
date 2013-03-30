<?php
    session_start();
    $username = $_POST['username'];
    $password = $_POST['password'];

    $_SESSION['username'] = $username;
    
    $HOST = 'localhost';
    $USERNAME = 'root';
    $PASSWORD = '';
    $DB = 'c203';

    $link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);

    $query = "SELECT * FROM repo_users WHERE username = '$username' AND password = SHA1('$password')";
    // echo $query.'<br>';
    $result = mysqli_query($link, $query) or die (mysqli_error($link));

    $row = mysqli_num_rows($result);

    if ($row > 0)
    {
        $msg = "You have logged in successfully";
        echo '<meta http-equiv="refresh" content="2;url=memberHome.php">';
    }
    else
    {
        $msg = "Your login has failed, please try again";
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>RePo - Login</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>RePo - Login</h3>
  <?php
  	echo $msg;
  ?>
</body>
</html>