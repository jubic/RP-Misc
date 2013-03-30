<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<title>Road Trip</title>
	</head>
	<body>
		<h1>Road Trip</h1>
		<hr />
		<form name="Form1" method="post" action="result.php">
                    <table border="0">
                    <tr>
                    <td><label for="myname">Your name:</label></td>
                        <td><input name="myname" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="temperature">Temperature of next location in Fahrenheit:</label></td>
                        <td><input name="temperature" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="distance">Distance to next location in miles:</label></td>
                        <td><input name="distance" type="text"></td>
                    </tr>

                    <tr>
                    <td><label for="speed">Maximum Speed in miles per hour:</label></td>
			<td><input name="speed" type="text"></td>
                    </tr>

                    <tr>
                    <td><p><label for="gallon">Gallon:</label></td>
                        <td><input name="gallon" type="text"></td>
                    </tr>

                    <tr>
                    <td>&nbsp;</td>
                    <td><input name="btnsubmit" value="Submit" type="submit"><input type="reset" value="Reset"></td>
                    </tr>
                    </table>
		</form>
	</body>
</html>