<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Lappos.com</title>
	</head>
	<body>
		<h1>Lappos.com</h1>
		<hr>
                    <a href="index.php">Home</a>
		<hr>
		<h2>Add New Design</h2>
		<fieldset>
                    <legend>Design Details</legend>
                    <form method='post' action='doAddDesign.php' enctype='multipart/form-data'>
                        <table>
                            <tr>
                                <td><label for='name'>Design Name:</label></td>
				<td><input type='text' name='name' id='name'/></td>
                            </tr>
                            <tr>
				<td><label for='designer'>Designer:</label></td>
				<td><input type='text' name='designer' id='designer'/></td>
                            </tr>
                            <tr>
				<td><label for='price'>Price:</label></td>
				<td><input type='text' name='price' id='price' /></td>
                            </tr>
                            <tr>
                                <td><label for='image'>Image:</label></td>
                                <td><input type='file' name='image' id='image' /></td>
                            </tr>
                            <tr>
				<td colspan='2' align='center'><input type='submit' value='Submit' /></td>
                            </tr>
                        </table>
                    </form>
                </fieldset>
	</body>
</html>
