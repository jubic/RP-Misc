<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $getTitle = $_POST['getTitle'];

        $host = "localhost";
        $user = "root";
        $pass = "";
        $db = "c203";

        // open connection
        $link = mysqli_connect($host, $user, $pass, $db);

        // build SQL statement
        $query = "SELECT * FROM music WHERE title LIKE '%$getTitle%'";

        // execute SQL statement
        $result = mysqli_query($link, $query) or die(mysqli_error($link));

        mysqli_close($link);

        while (
        $row=mysqli_fetch_array($result)){
            echo "Song Title: ";
            echo $row['title'];
            echo "<br>";
            echo "Song Album: ";
            echo $row['album'];
            echo "<br>";
            echo "Song Artist: ";
            echo $row['artist'];
            echo "<br>";
            echo "Song Rating: ";
            echo $row['rating'];
            echo "<br>";
            echo "Review: ";
            echo $row['review'];
        }
        
        ?>
    </body>
</html>