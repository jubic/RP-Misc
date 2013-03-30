<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Welcome</title>
</head>

<body>

    <?php

        print_r($_POST['name']);
        print_r($_POST['age']);
        print_r($_POST['email']);

    ?>

    <form method="post" action="">
        Name<input type="text" name="name" />
        Age<select name="age">
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
           </select>
        Email<input type="text" name="email" />
        <input type="submit" />
    </form>
</body>
</html>