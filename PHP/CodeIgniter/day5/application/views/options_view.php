<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>CRUD Operations</title>
        <style type="text/css">
            label {
                display:block;
            }
        </style>
    </head>
    <body>
        <h2>Create</h2>
        <?php echo form_open('site/create'); ?>
        <p>
            <label for="title">Title:</label>
            <?php
            $data = array(
                'name' => 'title',
                'id' => 'title',
            );
            echo form_input($data);
            ?>
        </p>

        <p>
            <label for="contents">Content:</label>
            <?php
            $data = array(
                'name' => 'contents',
                'id' => 'contents',
            );
            echo form_textarea($data);
            ?>
        </p>

        <p>
            <?php echo form_submit('submit', 'Submit'); ?>
        </p>
        <?php echo form_close(); ?>

            <hr/>

            <h2>Read</h2>

        <?php echo form_open('site/update'); ?>
        <?php if (isset($records)) :
                foreach ($records as $record) : ?>
                    <h2><?php echo anchor("site/delete/$record->id", $record->title); ?></h2>
        <?php echo form_hidden('id', $record->id); ?>
        <?php echo form_textarea('contents', $record->contents); ?>
        <?php endforeach; ?>
        <?php else : ?>
                        <h2>No records were returned.</h2>
        <?php endif; ?>
                        <p>
            <?php echo form_submit('submit', 'Edit'); ?>
                    </p>
        <?php echo form_close(); ?>

        <hr/>

        <h2>Delete</h2>

        <p>
            To sample the delete method, simply click on one of the headings listed above. A delete query will automatically run.
        </p>

        <hr/>

        <h2>Update</h2>

        <p>
            To sample the update method, simply edit one of the textareas and click on Edit.
        </p>
    </body>
</html>
