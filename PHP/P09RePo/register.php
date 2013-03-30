<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>RePo - Where RP comes together!</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>RePo - Register</h3>
  <h4>Please fill the following to sign up for RePo.</h4>
  <form method="post" action="doRegister.php">
  	<fieldset>
  		<legend>Registration Info</legend>
  		<table>
			<tr>
				<td><label for="name">Name:</label></td>
				<td><input type="text" id="name" name="name" /></td>
			</tr>
			<tr>
				<td><label for="gender">Gender:</label></td>
				<td><input type="text" id="gender" name="gender"/></td>
			</tr>
			<tr>
				<td><label for="birthdate">Birthdate:</label></td>
				<td><input type="text" id="birthdate" name="birthdate"/></td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td><label for="username">Username:</label></td>
				<td><input type="text" id="username" name="username"/></td>
			</tr>
			<tr>
				<td><label for="password1">Password:</label></td>
				<td><input type="password" id="password1" name="password1"/></td>
			</tr>
                        <tr>
                                <td><label for="password2">Enter Password Again:</label></td>
                                <td><input type="password" id="password2" name="password2"/></td>
                        </tr>
  		</table>	
  	</fieldset>
	<input type="submit" value="Sign Up" name="submit"/>
  </form> 
</body>
</html>
