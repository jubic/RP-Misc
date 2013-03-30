<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Day 1</title>
    </head>
    <body>
        <div id="container">
            <p>My view has been loaded</p>

            <?php foreach ($records as $row) : ?>
                <h1><?php echo $row->title; ?></h1>
            <?php endforeach; ?>
        </div>
    </body>
</html>
