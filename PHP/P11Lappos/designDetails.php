<?php

    $detailID = $_GET['id'];
    
    include 'dbFunctions.php';
    $arrDesignDetails = executeSelectQuery("SELECT * FROM lappos WHERE id = '$detailID'");

    $name = $arrDesignDetails[0]['name'];
    $designer = $arrDesignDetails[0]['designer'];
    $design = $arrDesignDetails[0]['image'];
    $price = $arrDesignDetails[0]['price'];

?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Lappos.com</title>
	</head>
	<body>
        <a href="index.php">Back to Design List</a>
            <h1><?php echo $name;?></h1>
            <table border=1 cellpadding=0 cellspacing=0>
                <tr>
                    <td rowspan="2"><img src="designs/<?php echo $design;?>"/></td>
                    <td>Designer:</td>
                    <td><?php echo $designer ;?></td>
                </tr>
                <tr>
                    <td>Price:</td>
                    <td><?php echo $price ;?></td>
                </tr>
            </table>
	</body>
</html>
