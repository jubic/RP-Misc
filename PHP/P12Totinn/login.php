<?php
session_start();
include 'dbFunctions.php';
$error_msg = "";
if(!isset($_SESSION['user_id'])){
	if(isset($_POST['username'])){
		//retrieve form data
		$username = $_POST['username'];
		$password = $_POST['password'];

                //match the username and password entered with database record
                $loginQuery = "SELECT user_id,username,role FROM users WHERE username='".$username."'AND password = SHA1('".$password."')";
                $arrUser = executeSelectQuery($loginQuery);

                //if record is found, store id and username into session
                if(count($arrUser) > 0){
                    $row = $arrUser[0];
                    $_SESSION['user_id'] = $row['user_id'];
                    $role = $row['role'];
                    $_SESSION['role'] = $role;
                    $authenticated = true;
                }else{
                    //record not found
                    $authenticated = false;
                }

		//if record is found, store id and username into session
		if($authenticated){
			$msg = '<p><i>Hi, '.$username.'!<br />';
			$msg .= 'You are logged in as a '.$_SESSION['role'].'<br /><a href="index.php">Home</a></p>';
                        if(isset($_POST['remember'])) {

                            setcookie('username', $username, time()+60*60*24*365*10);
                            setcookie('password', sha1($password), time()+60*60*24*365*10);

                        }
		}else{ //record not found
			$msg = '<p class="error">Sorry, you must enter a valid username and password to log in.<a href="index.php">Back</a></p>';
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
<title>Totinn - Login</title>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<h3>Totinn - Login</h3>
<?php
echo $msg;
?>
</body>
</html>