<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Times - Multiplication Table</title>
    </head>
    <body>
        <h1>Times - Multiplication Table</h1>
		<hr />
		<form method="post" action="timesTableOutput.php">
                    <table border="0">
                        <tr>
                        <td><label for="table">Which multiplication table would you like?</label></td>
                            <td><input name="table" type="text"></td>
                        </tr>

                        <tr>
                        <td><label for="max">How high do you want to go?</label></td>
                            <td><input name="max" type="text"></td>
                        </tr>

                        <tr>
                        <td>&nbsp;</td>
                        <td><input value="Submit" type="submit"><input type="reset" value="Reset"></td>
                        </tr>
                    </table>
		</form>
    </body>
</html>
