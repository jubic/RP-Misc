<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>OurConnection - Where the neighborhood comes together!</title>
        
    </head>
    <body>
        <h3>OurConnection - Register</h3>
        <h4>Please fill the following to sign up for OurConnection.</h4>
        <form method="post" action="doRegister.php">
            <fieldset>
                <legend>Registration Info</legend>
                <table>
                    <tr>
                        <td><label for="name">Name:</label></td>
                        <td><input type="text" name="name" /></td>
                    </tr>
                    <tr>
                        <td><label for="gender">Gender:</label></td>
                        <td>
                            <input type="radio" name="gender" value="male"/>male
                            <input type="radio" name="gender" value="female"/>female
                        </td>
                    </tr>
                    <tr>
                        <td><label for="birthdate">Birthdate:</label></td>
                        <td><input type="text" name="birthdate"/> (format: YYYY-MM-DD)</td>
                    </tr>
                    <tr>
                        <td colspan="2"><hr /></td>
                    </tr>
                    <tr>
                        <td><label for="username">Username:</label></td>
                        <td><input type="text" id="username" name="username"/></td>
                    </tr>
                    <tr>
                        <td><label for="password">Password:</label></td>
                        <td><input type="password" id="password" name="password"/></td>
                    </tr>
                    <tr>
                        <td><label for="color">Favorite Color</label></td>
                        <td><select name="color" size="1">
                            <option selected="selected" disabled="disabled">Select...</option>
                            <option value="red">Red</option>
                            <option value="green">Green</option>
                        </select></td>
                    </tr>
                    <tr>
                        <td><label for="phrase">Favourite Phrase:</label></td>
                        <td><input type="text" id="phrase" name="phrase"/></td>
                    </tr>
                </table>	
            </fieldset>
            <input type="submit" value="Sign Up" name="submit"/>
        </form> 
    </body>
</html>
