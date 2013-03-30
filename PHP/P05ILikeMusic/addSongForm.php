<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>iLikeMusic</title>
    </head>
    <body>
        <h1>Add Song</h1>
        <hr/>
        <form name="addSong" method="post" action="insertSongIntoDatabase.php">
                    <table border="0">
                    <tr>
                    <td><label for="title">Song Title:</label></td>
                        <td><input name="title" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="album">Album:</label></td>
                        <td><input name="album" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="artist">Artist:</label></td>
                        <td><input name="artist" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="rating">Rating:</label></td>
			<td><select name="rating">

                            <option value=" " selected="selected"> </option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>

                            </select>
                        </td>
                    </tr>

                    <tr>
                    <td><label for="review">Review</label></td>
                        <td><input name="review" type="text"></td>
                    </tr>

                    <tr>
                    <td>&nbsp;</td>
                    <td><input name="btnsubmit" value="Submit" type="submit"><input type="reset" value="Reset"></td>
                    </tr>
                    </table>
		</form>
    </body>
</html>
