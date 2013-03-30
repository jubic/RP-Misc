<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Registration</title>
        <script src="validate.js" type="text/javascript"></script>
    </head>
    <body>
        <h1>Registration</h1>
        <form method="post" action="doRegister.php" onSubmit="return validate(this);">
            <fieldset>
                <legend>Member Information</legend>
                <table>
                    <tr>
                        <td><label for="full_name">Full Name</label></td>
                        <td><input type="text" name="full_name" id="full_name"></td>
                    </tr>
                    <tr>
                        <td><label for="nric">NRIC</label></td>
                        <td><input type="text" name="nric" id="nric"></td>
                    </tr>
                    <tr>
                        <td><label for="dob">Date of Birth</label></td>
                        <td><input name="dob" id="dob" type="text" size="25"></td>
                    </tr>
                    <tr>
                        <td><label for="email">Email</label></td>
                        <td><input type="text" name="email" id="email"></td>
                    </tr>
                    <tr>
                        <td><label for="contact_no">Contact Number</label></td>
                        <td><input type="text" name="contact_no" id="contact_no"></td>
                    </tr>
                    <tr>
                        <td><label for="address">Address</label></td>
                        <td><textarea name="address" id="address" cols="16" rows=""></textarea></td>
                    </tr>
                    <tr>
                        <td><label for="postal_code">Postal Code</label></td>
                        <td><input type="text" name="postal_code" id="postal_code"></td>
                    </tr>
                </table>
            </fieldset>
            <fieldset>
                <legend>Account Details</legend>
                <table>
                    <tr>
                        <td><label for="username">Username</label></td>
                        <td><input type="text" name="username" id="username"</td>
                    </tr>
                    <tr>
                        <td><label for="password">Password</label></td>
                        <td><input type="password" name="password" id="password"</td>
                    </tr>
                    <tr>
                        <td><label for="confirm_password">Confirm Password</label></td>
                        <td><input type="password" name="confirm_password" id="confirm_password"</td>
                    </tr>
                </table>
            </fieldset>
            <fieldset>
                <table>
                    <tr>
                        <td><input type="submit" value="Register">  </td>
                    </tr>
                </table>
            </fieldset>
        </form>
    </body>
</html>
