<?php
session_start();

if(!isset($_SESSION['user_id'])){
	echo "You have not logged in.<br/>";
	echo "Please <a href='login.php'>login</a>.";
	exit;
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Post Sale Items</title>
	</head>
	<body>
		<h1>Post Sale Items</h1>
		<a href='index.php'>Home</a>
		<hr />
		<form method='post' action='doPostSaleItem.php'>
		<table border="1">
			<tr>
				<td><label for='itemName'>Item Name:</label></td>
				<td><input type='text' name='itemName' id='itemName' /></td>				
			</tr>
			<tr>
				<td><label for='itemDescription'>Item Description:</label></td>
				<td><textarea name='itemDescription' id='itemDescription'></textarea></td>	
			</tr>
			<tr>
				<td><label for='itemPrice'>Item Price:</label></td>
				<td><input type='text' name='itemPrice' id='itemPrice' /></td>	
			</tr>
			<tr>
				<td colspan='2' align='center'><input type='submit' value='Post Item' /></td>	
			</tr>
		</table>
		</form>
	</body>
</html>