<?php
session_start();
include 'dbFunctions.php';

if(isset($_COOKIE['username']) && isset($_COOKIE['password'])) {

    $username = $_COOKIE['username'];
    $password = $_COOKIE['password'];

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

}

elseif(isset($_SESSION['user_id'])) {

    $getUserQuery = "SELECT username FROM users WHERE user_id=".$_SESSION['user_id'];
    $arrUser = executeSelectQuery($getUserQuery);
    $username = $arrUser[0][0];

}

?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Totinn - Home</title>
    </head>
    <body bgcolor="<?php echo $_COOKIE['colour']; ?>">
        <p><a href="customize.php">Customize Background Colour</a></p>
        <?php
        if(isset($_SESSION['user_id']))
        {
        ?>
            <h2>Welcome back, <i><?php echo $username; ?></i>!</h2>
            <a href="logout.php">Logout</a>
        <?php
        }
        else
        {
        ?>
            <form name="loginForm" method="post" action="login.php">
                <table>
                    
                    <tr>

                        <td align="center"><label for="username">Username</label></td>
                        <td><input type="text" id="username" name="username" /></td>

                    </tr>

                    <tr>
                        
                        <td align="center"><label for="password">Password</label></td>
                        <td><input type="password" id="password" name="password" /></td>

                    </tr>
                        
                    <tr>

                        <td colspan="2" align="left"><input type="checkbox" name="remember">Keep Me Logged In</td>

                    </tr>

                    <tr>

                        <td colspan="2" align="left"><a href="forgotPassword.php">Forgot Password</a></td>

                    </tr>

                    <tr>
                        
                        <td colspan="2" align="center"><input type="submit" name="Login" value="Login"/></td>

                    </tr>
                </table>
        </form>
        <?php
        }
        ?>
    </body>
</html>
