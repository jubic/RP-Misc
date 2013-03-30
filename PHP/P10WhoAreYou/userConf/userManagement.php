<?php
session_start();
if(isset($_SESSION['user_id'])){
    $HOST = 'localhost';
    $USERNAME = 'root';
    $PASSWORD = '';
    $DB = 'c203';

    $link = mysqli_connect($HOST,$USERNAME,$PASSWORD,$DB);
    $sql = "SELECT user_id,username,role FROM users WHERE role ='member' OR role = 'moderator'";
    $result = mysqli_query($link,$sql) or die(mysqli_error($link));

    while($row = mysqli_fetch_array($result))
    {
        $arrUsers[] = $row;
    }
}
else
{
    $message = "You are not logged in.";
}
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
    <a href="../index.php">Home</a>
<h1>Boomdosh Users</h1>
<?php
    if(isset($_SESSION['user_id'])){
?>
<table border='1'>
	<tr>
	<th>ID</th>
	<th>Username</th>
	<th>Assignment</th>
	</tr>
<?php
	for($countUsers=0;$countUsers<count($arrUsers);$countUsers++)
        {
            $userID = $arrUsers[$countUsers]['user_id'];
            $username = $arrUsers[$countUsers]['username'];
            $role = $arrUsers[$countUsers]['role'];
?>
        <tr>
            <td><?php echo $userID; ?></td>
            <td><?php echo $username; ?></td>
<?php
            if ($role == 'Member')
            {
?>
            <td>
                <form method='post' action='assignAsModerator.php'>
                    <input type='hidden' name='userID' value='<?php echo $userID; ?>' />
                    <input type='submit' value='Assign As Moderator' />
                </form>
            </td>
<?php
            }
            elseif ($role == 'Moderator')
            {
?>
            <td>
                <form method='post' action='assignAsMember.php'>
                    <input type='hidden' name='userID' value='<?php echo $userID; ?>' />
                    <input type='submit' value='Assign As Member' />
                </form>
            </td>
<?php
            }
?>
        </tr>
<?php
	}
?>
        </table>
<?php
    }
    else
    {
?>
<h3><?php echo $message; ?></h3>
<?php
    }
?>
    </body>
</html>