<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>OurConnection - Where the neighborhood comes together!</title>

    </head>
    <body>
        <a href="login.php">Login |</a> <a href="register.php">Register |</a>
        <h3>Our Connection - Login</h3>
        <h4>Please Login to Our Connection.</h4>
        <form method="post" action="doLogin.php">
            <fieldset>
                <legend>Login Info</legend>
                <table>
                    <tr>
                        <td><label for="username">Username:</label></td>
                        <td><input type="text" id="username" name="username"/></td>
                    </tr>

                    <tr>
                        <td><label for="password">Password:</label></td>
                        <td><input type="password" id="password" name="password"/></td>
                    </tr>
                </table>	
            </fieldset>
            <input type="submit" value="Login" name="submit"/>
        </form> 
    </body>
</html>