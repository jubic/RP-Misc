<?php
include "dbFunctions.php";

$nric = $_POST['nric'];
$dob = $_POST['demo1'];
$email = $_POST['email'];
$contactNo = $_POST['contact_no'];
$username = $_POST['username'];
$password = $_POST['password'];

function convertDate($date) {
    $dateArray = explode("-", $date);
    $newDate = $dateArray[2] . "-" . $dateArray[1] . "-" . $dateArray[0];
    return $newDate;
}

//echo convertDate($dob);
$checkQuery = "SELECT * from member where username = '$username'";
$checkResult = mysqli_query($link, $checkQuery) or die(mysqli_connect_error($link));
$row = mysqli_fetch_array($checkResult); 
$inserted = '';
if(mysqli_num_rows($checkResult)==0){
$insertQuery = "INSERT INTO member (nric,dob,email,contact_no,username,password)
    VALUES ('" . $nric . "','" . convertDate($dob) . "','" . $email . "','" . $contactNo . "','" . $username . "',SHA1('" . $password . "'))";
$inserted = mysqli_query($link, $insertQuery) or die(mysqli_error($link));

if($inserted){
    $message = "Registration submitted successfully";
    
}else{
    die ("Registration submission failed" .mysqli_error($link));
}  
}else{
    $message = "The Username is already existed, please create a new Username.";
}
?>
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <h3>
        <?php
            echo $message;
        ?>
        </h3>
        <?php if($inserted)
        {
        ?>
        <table>
            <tr>
                <th>NRIC: </th>
                <td><?php echo $nric; ?></td>
            </tr>
            
            <tr>
                <th>Date of Birth: </th>
                <td><?php echo $dob; ?></td>
            </tr>
            <tr>
                <th>Email: </th>
                <td><?php echo $email; ?></td>
            </tr>
            <tr>
                <th>Contact Number: </th>
                <td><?php echo $contactNo; ?></td>
            </tr>
            
            
        </table>
        <?php
        }
        ?>
        <a href ="index.php">Back</a>
    </body>
</html>
