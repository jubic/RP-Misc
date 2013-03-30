 <?php 
    $username = $_POST['username'];
    $password = $_POST["password"];

    $host = 'localhost';
    $username1 = 'root';
    $password1 = '91503149';
    $db = 'c203_p06';
    $link = mysqli_connect($host,$username1,$password1,$db);

    $query = "SELECT * FROM users WHERE username ='$username' AND password = SHA1 ('$password')";
    $result = mysqli_query($link,$query) or die(mysqli_error($link));


    if (mysqli_num_rows($result) == 1){
        session_start();
        $row = mysqli_fetch_array($result);
        $_SESSION['username'] = $row['username'];
        $_SESSION['favourite_color'] = $row['favourite_color'];
        $_SESSION['favourite_phrase'] = $row['favourite_phrase'];
    } else{
        echo '<p> Sorry, You must enter a vaild username or password to login. <a href="login.php" target="_blank">Back</a>';
    }
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>OurConnection - Where the neighborhood comes together!</title>

</head>
<body style="background-color:<?php echo $_SESSION['favourite_color'];?>">
    <h1>OurConnection - Login</h1>

    <?php 
    echo '<p> You are logged in as '.$username.'.</p>';
    echo '<p><b>'.$_SESSION['favourite_phrase'].'</b></p>';
    echo '<a href="index.php" target="_blank">Home</a>';
    mysqli_close($link);
    ?>

</body>
</html>