<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Boomdosh</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<h3>Boomdosh - Login</h3>
<p><a href='index.php'>Home</a></p>
<!-- Username and Password posted to doLogin.php -->
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
<tr>
<td><input type="submit" Value="Login"/></td>
</tr>
</table>
</fieldset>
</form>
</body>
</html>
