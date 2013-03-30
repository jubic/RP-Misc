<?php

    $message = 'You have logged out';

    session_start();
    if (isset($_SESSION['username']))
    {
        $_SESSION = array();
            session_destroy();
            $msg = "You've logged out successfully";
    }
    
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>RePo - Logout</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>RePo - Logout</h3>
  <?php
  	echo $msg;
  ?>
  <meta http-equiv="refresh" content="2;url=index.php"/>
</body>
</html>