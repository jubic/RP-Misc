<?php
	session_start();
	$userID = $_SESSION['user_id'];
	if(isset($_POST['itemName'])){
		$itemName = $_POST['itemName'];
		$itemDescription = $_POST['itemDescription'];
		$itemPrice = $_POST['itemPrice'];
		
		$HOST = 'localhost';
		$USERNAME = 'root';
		$PASSWORD = '';
		$DB = 'c203';
		
		$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB) or die (mysqli_connect_error());
		
		$sql = "INSERT INTO sale_items (name,user_id,description,price) VALUES ('".$itemName."',".$userID.",'".$itemDescription."',".$itemPrice.")";
		$status = mysqli_query($link,$sql) or die(mysqli_error($link));
		
		if($status){
			$message = "Item posted successfully.<br />";
			$message .= "<a href='index.php'>Home</a>";
		}else{
			$message = "Item post failed.<br />";
			$message .= "<a href='postSaleItem.php'>Try Again.</a>";
		}
	}else{
		$message = "All item details have to be provided.<br />";
		$message .= "<a href='postSaleItem.php'>Try Again.</a>";
	}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Post Sale Items</title>
	</head>
	<body>
		<h1>Boomdosh - Post Item</h1>
			<p>
			<?php echo $message; ?>
			</p>
	</body>
</html>