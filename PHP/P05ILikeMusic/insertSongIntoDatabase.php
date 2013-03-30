<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>iLikeMusic</title>
    </head>
    <body>
        <?php
        $insertTitle = $_POST['title'];
        $insertAlbum = $_POST['album'];
        $insertArtist = $_POST['artist'];
        $insertRating = $_POST['rating'];
        $insertReview = $_POST['review'];

        $link = mysqli_connect('localhost', 'root', '', 'c203') or die(mysqli_connect_error());

        $query = "INSERT INTO music(title,album,artist,rating,review) VALUES ('$insertTitle','$insertAlbum','$insertArtist','$insertRating','$insertReview')";

        $result = mysqli_query($link, $query) or die('Error querying database');

        mysqli_close($link);
        ?>
    </body>
</html>
