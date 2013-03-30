<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Boomdosh - Sell It Here!</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>Boomdosh - Register</h3>
  <p><a href='index.php'>Home</a></p>
  <h4>Please fill the following to sign up for Boomdosh.</h4>
  <form method="post" action="doRegister.php">
  	<fieldset>
  		<legend>Registration Info</legend>
  		<table>
			<tr>
				<td><label for="username">Username:</label></td>
				<td><input type="text" id="username" name="username"/></td>
			</tr>
			<tr>
				<td><label for="password1">Password:</label></td>
				<td><input type="password" id="password1" name="password1"/></td>
			</tr>
			<tr>
				<td><label for="password2">Password (retype):</label></td>
				<td><input type="password" id="password2" name="password2"/></td>
			</tr>
  		</table>	
  	</fieldset>
	<input type="submit" value="Sign Up" name="submit"/>
  </form> 
</body>
</html>
