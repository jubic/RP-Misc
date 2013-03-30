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
  <title>RePo - Where RP comes together!</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>RePo - Where RP comes together!</h3>
  <form method="post" action="doLogin.php">
  	<fieldset>
  		<legend>Login</legend>
		<table>
			<tr>
				<td><label for="username">Username:</label></td>
				<td><input type="text" id="username" name="username"/></td>
			</tr>
			<tr>
				<td><label for="password">Password:</label></td>
				<td><input type="password" id="password" name="password"/></td>
			</tr>
		</table>
  	</fieldset>
	<input type="submit" value="Login" name="submit"/>
  </form>
  <a href="register.php">Register</a>
</body>
</html>