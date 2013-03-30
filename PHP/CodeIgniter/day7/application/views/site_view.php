<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Pagination</title>
        <?php echo link_tag('css/style.css'); ?>
    </head>
    <body>
        <div id="container">
            <h1>Super Pagination with CodeIgniter</h1>
            <?php echo $this->table->generate($records); ?>
            <?php echo $this->pagination->create_links(); ?>
        </div>
    </body>
</html>
