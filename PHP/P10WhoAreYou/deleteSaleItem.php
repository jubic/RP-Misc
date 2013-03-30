<?php
    session_start();
    $itemID = $_POST['itemID'];

    if(isset($_SESSION['user_id'])){
        $HOST = 'localhost';
        $USERNAME = 'root';
        $PASSWORD = '';
        $DB = 'c203';

        $link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
        $sql = "DELETE FROM sale_items WHERE sale_item_id = '$itemID'";
        $result = mysqli_query($link,$sql) or die(mysqli_error($link));
    }
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Post Sale Items</title>
	</head>
	<body>
		<h1>Boomdosh - Delete Item</h1>
	</body>
</html>