<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Find Song</h1>
        <hr/>
        <form name="grabSong" method="post" action="grabSongFromDatabase.php">
            <table border="0">
                    <tr>
                    <td><label for="getSong">Song Title:</label></td>
                        <td><input name="getTitle" type="text"></td>
                    </tr>

                    <tr>
                    <td>&nbsp;</td>
                    <td><input name="btnsubmit" value="Submit" type="submit"><input type="reset" value="Reset"></td>
                    </tr>
            </table>
        </form>
    </body>
</html>
