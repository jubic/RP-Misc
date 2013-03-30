<?php
	session_start();
	$HOST = 'localhost';
	$USERNAME = 'root';
	$PASSWORD = '';
	$DB = 'c203';
	
	$link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
	if(!$link){
		die(mysqli_error($link));
	}
	
	$sql = "SELECT s.name,s.description,s.price,u.username,s.sale_item_id FROM sale_items s, users u WHERE s.user_id=u.user_id";
	$result = mysqli_query($link,$sql) or die(mysqli_error($conn));

        while($row=mysqli_fetch_array($result))
        {
            $arrItems[] = $row;
        }
        mysqli_close($link);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Boomdosh</title>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
  <h1>Boomdosh - Sell It Here!</h1>
  
<?php
	if(isset($_SESSION['user_id']))
        {
            if($_SESSION['role'] == 'Administrator')
            {
?>
                &loz;<a href="postSaleItem.php">Post Item For Sale</a><br />
                &loz;<a href="userConf/userManagement.php">User Management</a><br />
                &loz;<a href="logout.php">Logout</a><br />
<?php
            }
            
            elseif($_SESSION['role'] == 'Member' || $_SESSION['role'] == 'Moderator')
            {
?>
                &loz;<a href="postSaleItem.php">Post Item For Sale</a><br />
                &loz;<a href="logout.php">Logout</a><br />

<?php
            }
            
        }
        else
        {
?>
            &loz;<a href="register.php">Register</a><br />
            &loz;<a href="login.php">Login</a><br />
<?php
	}
?>
		<h3>Sale Items</h3>
		<table border="1">
                    <tr>
			<th>Name</th>
			<th>Description</th>
			<th>Price</th>
			<th>Owner</th>
<?php
                    if(isset($_SESSION['user_id']))
                    {
                        if($_SESSION['role'] == 'Moderator' || $_SESSION['role'] == 'Administrator')
                        {
?>
                            <th>Delete</th>
<?php
                        }
                    }
?>
                    </tr>
<?php
                for($countItem=0;$countItem<count($arrItems);$countItem++)
                {
                    $name = $arrItems[$countItem]['name'];
                    $description = $arrItems[$countItem]['description'];
                    $price = $arrItems[$countItem]['price'];
                    $owner = $arrItems[$countItem]['username'];
                    $saleItemID = $arrItems[$countItem]['sale_item_id'];
?>
                    <tr>
                        <td><?php echo $name; ?></td>
                        <td><?php echo $description; ?></td>
                        <td><?php echo $price; ?></td>
			<td><?php echo $owner; ?></td>
<?php
                    if(isset($_SESSION['user_id']))
                    {
                        if($_SESSION['role'] == 'Moderator' || $_SESSION['role'] == 'Administrator')
                        {

?>
                        <td>
                            <form method='post' action='deleteSaleItem.php'>
                                <input type='hidden' name='itemID' value='<?php echo $saleItemID; ?>' />
                                <input type='submit' value='Delete Item' />
                            </form>
                        </td>
                    </tr>
<?php
                        }
                    }
                }
?>
		</table>
</body>
</html>