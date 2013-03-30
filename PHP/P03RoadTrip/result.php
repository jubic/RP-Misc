<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

        <head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<title>Road Trip</title>
	</head>

	<body>

                <h1>Road Trip</h1>

                       <?php

                        /*The built-in $_POST function is used to collect values from a form sent with method="post".

                        Information sent from a form with the POST method is invisible to others and has no limits on the amount of information to send.

                        Note: However, there is an 8 Mb max size for the POST method, by default (can be changed by setting the post_max_size in the php.ini file).*/

                        $myname = $_POST['myname'];
                        $tempInF = $_POST['temperature'];
                        $dist = $_POST['distance'];
                        $spd = $_POST['speed'];
                        $gallon = $_POST['gallon'];


                        $tempToC = (5/9 * ($tempInF-32));
                        $tempToC = (($tempInF-32) * 5/9);
                        $time = ($dist/$spd);
                        $litre = ($gallon*3.785);

                        echo "<br>"."Hi ".$myname."!";
                        echo "<br>".$tempInF." degrees Fahrenheit = ".$tempToC." degrees Celsius.";
                        echo "<br>"."It will take ".$time." hours to drive ".$dist." at ".$spd."  miles per hour.";
                        echo "<br>".$gallon." Gallons = ".$litre." litre.";
                    ?>

                    <form action="">
                    <input type="button" value="Back" onclick="history.go(-1);"></input>
                    </form>

        </body>
    
</html>