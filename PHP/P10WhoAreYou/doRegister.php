<?php
	if(isset($_POST['username'])){
		$username = $_POST['username'];
		$password1 = $_POST['password1'];
		$password2 = $_POST['password2'];
		
		$HOST = 'localhost';
		$USERNAME = 'root';
		$PASSWORD = '';
		$DB = 'c203';
		
		$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
		
		if($password1 == $password2){
			$query = "INSERT INTO users(username,password,role) VALUES ('".$username."',SHA1('".$password1."'), 'Member')";
			$status = mysqli_query($link,$query) or die(mysqli_error($link));
			if($status){
			$message = '<p>Your new account has been successfully created. You are now ready to <a href="login.php">login</a>.</p>';
			$message .= '<p><a href="index.php">Home</a></p>';
			}
		}else{
			$message = '<p class="error">Passwords do not match.<a href="register.php">Back</a></p>';
		}
	}else {
		$message = '<p class="error">You must enter all of the sign-up data, including the desired password twice.<a href="register.php">Back</a></p>';
	}
	mysqli_close($link);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Boomdosh - Register</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h3>Boomdosh - Register</h3>
  <?php
  	echo $message;
  ?>
</body>
</html>