<?php
include 'dbFunctions.php';

if(isset($_POST)) {
    
    $nric = clean($_POST['nric']);
    $fullName = clean($_POST['full_name']);
    $dob = clean($_POST['dob']);
    $email = clean($_POST['email']);
    $contactNo = clean($_POST['contact_no']);
    $address = clean($_POST['address']);
    $postalCode = clean($_POST['postal_code']);
    $username = clean($_POST['username']);
    $password = clean($_POST['password']);

    //Test for duplicate username
    $duplicate = "SELECT * FROM member WHERE username = '$username'";
    $duplicateResult = executeSelectQuery($duplicate);

    if(count($duplicateResult) == 0) {

        $insertQuery = "INSERT INTO member VALUES ('".$nric."','".$fullName."','".$dob."','".$email."','".$contactNo."','".$address."','".$postalCode."','".$username."',SHA1('".$password."'))";
        $inserted = executeInsertQuery($insertQuery);

        if($inserted) {

            $message = "Registration submitted successfully";

        }

        else {

            $message = "Registration submission failed";

        }

    }
    else {

        $message = "Duplicate username(s) found in database";

    }

}
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
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
                <th>NRIC</th>
                <td><?php echo $nric; ?></td>
            </tr>
            <tr>
                <th>Full Name</th>
                <td><?php echo $fullName; ?></td>
            </tr>
            <tr>
                <th>Date of Birth</th>
                <td><?php echo $dob; ?></td>
            </tr>
            <tr>
                <th>Email</th>
                <td><?php echo $email; ?></td>
            </tr>
            <tr>
                <th>Contact Number</th>
                <td><?php echo $contactNo; ?></td>
            </tr>
            <tr>
                <th>Address</th>
                <td><?php echo $address; ?></td>
            </tr>
            <tr>
                <th>Postal Code</th>
                <td><?php echo $postalCode; ?></td>
            </tr>
        </table>
        <?php
        }
        ?>
    </body>
</html>
