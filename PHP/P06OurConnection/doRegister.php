<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Our Connection</title>
    </head>

    <body>
        <h1> Our Connection - Register</h1>
        <?php
        $host = 'localhost';
        $user = 'root';
        $pw = "91503149";
        $db = "c203_p06";
        
        $name = $_POST['name'];
        $gender = $_POST['gender'];
        $birthdate = $_POST['birthdate'];
        $username = $_POST['username'];
        $password = $_POST['password'];
        $color = $_POST['color'];
        $phrase = $_POST['phrase'];
        
        $link = mysqli_connect($host, $user, $pw, $db);

        $duplicate = "SELECT * FROM users WHERE username = '$username'";
        $duplicateResult = mysqli_query($link, $duplicate) or die(mysqli_error());
        $duplicateRows = mysqli_num_rows($duplicateResult);

        if($duplicateRows == 0) {
            $register = "INSERT INTO users(username,password,name,gender,birthdate,favourite_color,favourite_phrase) VALUES ('$username', SHA1('$password'), '$name', '$gender', '$birthdate', '$color', '$phrase')";
            $result = mysqli_query($link, $register) or die(mysqli_error($link));
            echo 'Your new account has been successfully created. You are now to ready to <a href="login.php">login</a>';
        }
        else{
        ?>
        <script type="text/javascript">
            alert("Username exists in the database already, please choose another. Bitch!");
            window.location.href="register.php";
        </script>
        <?php
        }
        mysqli_close($link);
        ?> 
    </body>
</html>
