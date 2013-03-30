<?php

    include ('dbFunctions.php');

    $newPwd = createRandomPassword();

    $user = $_POST['username'];
    $email = $_POST['email'];

    $updatePwd = "UPDATE users SET password = sha1('$newPwd') WHERE username = '$user'";

    $status = executeUpdateQuery($updatePwd);

    if ($status) {
        
        //send mail
        $to = $email;
        $subject = "New Password";
        $message = "Hello! Your password has been changed to ".$newPwd;
        $from = "no-reply@sit.rp.edu.sg";
        $headers = "From: $from";
        mail($to,$subject,$message,$headers);
        $statusMessage = "Mail Sent.";
        $statusMessage .= '<meta http-equiv="refresh" content="2;url=index.php">';
        
    }

    else {

        $statusMessage = "Mail not sent";

    }
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <p>
        <?php
            echo $statusMessage;
        ?>
        </p>
    </body>
</html>
