<?php
    include 'dbFunctions.php';
    $arrDesigns = executeSelectQuery("SELECT * FROM lappos");
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Lappos.com</title>
	</head>
	<body>
		<h1>Lappos.com</h1>
                <hr/>
                    <a href="addDesign.php">Add New Design</a>
		<hr/>
		<h2>Laptop Skins</h2>
		<table border='1' cellpadding='0' cellspacing='0'>
<?php
	for($countDesigns=0;$countDesigns<count($arrDesigns);$countDesigns++)
        {
            $name = $arrDesigns[$countDesigns]['name'];
            $image = $arrDesigns[$countDesigns]['image'];
            $id = $arrDesigns[$countDesigns]['id'];
?>
                    <tr>
                        <td><img src="designs/<?php echo $image;?>" width="120px"/></td>
                        <td><a href="designDetails.php?id=<?php echo $id ;?>"><?php echo $name ;?></a>
                    </tr>
<?php
	}
?>		
		</table>
	</body>
</html>
