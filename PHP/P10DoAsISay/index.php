<!DOCTYPE HTML>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Registration</title>
    <script language="javascript" type="text/javascript" src="datetimepicker.js"></script>

    <script type="text/javascript">
    function validate(form)
    {
        var NRIC = form.nric.value;
        var username = form.username.value;
        var email = form.email.value;
        var contact_no=form.contact_no.value;
        var password = form.password.value;
        var confirm_password = form.confirm_password.value;
        
        var RE_NRIC = /^[S]{1}[0-9]{7}[A-Z]{1}$/;
        var RE_USERNAME = /^[A-Za-z\d]{6,15}$/;
        var RE_EMAIL = /^(\w+[\-\.])*\w+@(\w+\.)+[A-Za-z]+$/;
        var RE_CONTACT_NO = /^[6|8|9]{1}[0-9]{7}$/;
        var RE_PASSWORD = /^[A-Za-z\d]{6,}$/;
        
        
        errors = [];
        
        if (!RE_NRIC.test(NRIC))
        {
            errors[errors.length] ="NRIC is invalid";								
        }
        
        if (!RE_USERNAME.test(username))
        {
            errors[errors.length] = "Username is invalid. ** It must be between 6-15 letters or digits. **";								
        }
        
                //the rest of if statements
                if (!RE_EMAIL.test(email)) {
                    errors[errors.length] = "User email address is invalid.";
                }
                
                if (!RE_CONTACT_NO.test(contact_no)) {
                    errors[errors.length] = "User contact number is invalid. ** It must be a valid 8 digits mobile/residential number. **";
                }
                if (!RE_PASSWORD.test(password)) {
                    errors[errors.length] = "User password is invalid. ** It must have at least 6 characters, contain both letters and digits. **";
                }		
                if (confirm_password != password) {
                    errors[errors.length] = "Please enter the same password again to confirm your password.";
                }
                if (errors.length > 0)
                {
                    reportErrors(errors);
                    return false;	
                }
                return true;						
            }
            function reportErrors(errors){
                var msg = "You have some problems: \n";
                for (var i = 0; i<errors.length; i++) {
                    var numError = i + 1;
                    msg += " \n" + numError + " . " + errors[i];
                }
                alert(msg);
            }
            
            </script>

        </head>
        <body>
            <h1>Registration</h1>
            <form method="post" action="doRegister.php" onSubmit="return validate(this);">
                <fieldset>
                    <legend>Member Information</legend>
                    <table>
                        <tr>
                            <td><label for="nric">NRIC</label></td>
                            <td><input type="text" name="nric" id="nric"></td>
                        </tr>
                        <tr>
                            <td><label for="demo1">Date of Birth</label></td>
                            <td><input id="demo1" name="demo1" type="text" size="25"><a href="javascript:NewCal('demo1','ddmmyyyy')"><img src="cal.gif" width="16" height="16" border="0" alt="Pick a date"></a></td>
                        </tr>
                        <tr>
                            <td><label for="email">Email</label></td>
                            <td><input type="text" name="email" id="email"></td>
                        </tr>
                        <tr>
                            <td><label for="contact_no">Contact Number</label></td>
                            <td><input type="text" name="contact_no" id="contact_no"></td>
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
