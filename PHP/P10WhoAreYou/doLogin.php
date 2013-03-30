<?php
session_start();
$error_msg = "";
if(!isset($_SESSION['user_id'])){
	if(isset($_POST['username'])){
		//retrieve form data
		$username = $_POST['username'];
		$password = $_POST['password'];

		//connect to database
		$HOST = 'localhost';
		$USERNAME = 'root';
		$PASSWORD = '';
		$DB = 'c203';
		
		$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);

		//match the username and password entered with database record
		$query = "SELECT user_id,username,role FROM users WHERE username='".$username."'AND password = SHA1('".$password."')";
		$result = mysqli_query($link,$query) or die(mysqli_error($link));

		//if record is found, store id and username into session
		if(mysqli_num_rows($result) == 	1){
			$row = mysqli_fetch_array($result);
			$_SESSION['user_id'] = $row['user_id'];
			$_SESSION['role'] = $row['role'];
                        
			$msg = '<p><i>Hi, '.$row['username'].'!<br />';
			$msg .= 'You are logged in as a '.$row['role'].'.<br /><a href="index.php">Home</a></p>';
		}else{ //record not found
			$msg = '<p class="error">Sorry, you must enter a valid username and password to log in.<a href="login.php">Back</a></p>';
		}
	}
}else{
	$msg = 'You are are already logged in.<br /><a href="index.php">Home</a></p>';
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Boomdosh - Login</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<h3>Boomdosh - Login</h3>
<?php
echo $msg;
?>
</body>
</html>