<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Our Connection </title>
        
    </head>
    <body>
        <h3>Our Connection - Log Out </h3>
        
        <?php
        session_start();
        if (isset($_SESSION['username'])){
        session_destroy();
        }
        ?>

        <p> You have logged out.</p>
        <a href="index.php">Home |</a>
        


    </body>
</html>