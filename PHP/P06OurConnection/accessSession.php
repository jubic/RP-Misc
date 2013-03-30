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
            echo '<p> You are logged in as ' . $username . '</p>';
        } else {
            echo '<p> Session is empty </p>';
        }
        ?>
    </body>
</html>