<?php

    include 'dbFunctions.php';
    $image = basename($_FILES['image']['name']);
    $tmpName = $_FILES['image']['tmp_name'];
    $targetPath = "designs/".$image;

    if (move_uploaded_file($tmpName, $targetPath)) {

        // Retrieve Form Data
        $name = $_POST['name'];
        $designer = $_POST['designer'];
        $price = $_POST['price'];
        $insertQuery = "INSERT INTO lappos(name, designer, price, image) VALUES('".$name."', '".$designer."', '".$price."', '".$image."')";
        $insertDesign = executeInsertQuery($insertQuery);

        if($insertDesign) {

            $message = "New design saved successfully";

        }

        else {

            $message = "Error saving new design";

        }

    }

    else {

        $message = "Problem uploading";
        
    }
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Lappos.com</title>
	</head>
	<body>
		<h1>Lappos.com</h1>
		<hr>
                    <a href="index.php">Home</a>
		<hr>
		<h2>Add New Design</h2>
		<?php echo $message; ?>
	</body>
</html>