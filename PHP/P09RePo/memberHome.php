<?php
    session_start();
    if (isset($_SESSION['username']))
    {
        $username = $_SESSION['username'];
        $msg = "<p>You have logged in as <b>".$username."</b></p>";
    }
    else
    {
        $msg = '<p> Session is empty </p>';
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>RePo - ShoutBox</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>RePo - Member Home</h3>
  <a href="index.php">Home</a> | <a href="logout.php">Log Out</a>
  <hr />
  <?php
    echo $msg;
  ?>
</body>
</html>