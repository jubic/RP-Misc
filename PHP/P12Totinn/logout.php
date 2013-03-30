<?php
    session_start();
    if(isset($_SESSION['user_id'])){
        $_SESSION = array();
        setcookie('username', $username);
        setcookie('password', $password);
        session_destroy();
        $message = '<p>You have logged out.<br /><a href="index.php">Back</a></p>';
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Totinn - Logout</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<h3>Totinn - Logout</h3>
<hr />
<?php
echo $message;
?>
</body>
</html>