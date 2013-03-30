<?php
	if(isset($_POST)){
		$name = $_POST['name'];
		$gender = $_POST['gender'];
		$birthdate = $_POST['birthdate'];
		$username = $_POST['username'];
		$password1 = $_POST['password1'];
                $password2 = $_POST['password2'];
		
		$HOST = 'localhost';
		$USERNAME = 'root';
		$PASSWORD = '';
		$DB = 'c203';
		
		$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);

		$query = "INSERT INTO repo_users(name,gender,birthdate,username,password) VALUES ('".$name."','".$gender."','".$birthdate."','".$username."',SHA1('".$password1."'))";
		$status = mysqli_query($link,$query) or die(mysqli_error($link));

                if($password1 == $password2){
                    if($status){
                        $message = '<p>Your new account has been successfully created. You are now ready to <a href="index.php">login</a>.</p>';
                        $message .= '<p><a href="index.php">Home</a>';
                    }
                }
                else if($password1 != $password2){
                    $message = 'Your password do not tally';
                }
	}
        else {
		$message = '<p class="error">You must enter all of the sign-up data.<a href="index.php">Back</a></p>';
                }
	mysqli_close($link);
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
  <title>RePo - Register</title>
  <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <h3>RePo - Register</h3>
  <?php
  	echo $message;
  ?>
</body>
</html>