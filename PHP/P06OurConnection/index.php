<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Our Connection - Home</title>

    </head>
    <body>        
        <?php
        session_start();
        if (isset($_SESSION['username'])) {
            $username = $_SESSION['username'];
            ?>
            <p> Our Connection - Member Home
                <p> Hi <?php echo $username ?></p>
                <a href="logout.php">Logout</a>

                <?php
            } else {
                ?>
                <p><h2> Our Connection</h2></p>
                <p> Please <a href="login.php">Log in</a></p>
                <p> <a href="register.php">Register</a></p>
                <?php
            }
            ?>
    </body>
</html>