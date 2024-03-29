<!DOCTYPE HTML>
<html>
    <head>
        <title>Films</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <style type="text/css">
            * {
                font-family: Arial;
                font-size: 12px;
            }
            table {
                border-collapse: collapse;
            }
            td, th {
                border: 1px solid #666666;
                padding:  4px;
            }
            div {
                margin: 4px;
            }
            .sort_asc:after {
                content: "▲";
            }
            .sort_desc:after {
                content: "▼";
            }
            label {
                display: inline-block;
                width: 120px;
            }
        </style>
    </head>
    <body>

        <?php echo form_open('films/search'); ?>
        <div>
            <?php echo form_label('Title:', 'title'); ?>
            <?php echo form_input('title', set_value('title'), 'id="title"'); ?>
        </div>

        <div>
            <?php echo form_label('Category:', 'category'); ?>
            <?php echo form_dropdown('category', $category_options,
                    set_value('category'), 'id="category"'); ?>
        </div>

        <div>
            <?php echo form_label('Length:', 'length'); ?>
            <?php
            echo form_dropdown('length_comparison',
                    array('gt' => '>', 'gte' => '>=', 'eq' => '=', 'lte' => '<=', 'lt' => '<'),
                    set_value('length_comparison'), 'id="length_comparison"'); ?>
<?php echo form_input('length', set_value('length'), 'id="length"'); ?>
        </div>

        <div>
<?php echo form_submit('action', 'Search'); ?>
        </div>

<?php echo form_close(); ?>

            <div>
    		Found <?php echo $num_results; ?> films
        </div>

        <table>
            <thead>
<?php foreach ($fields as $field_name => $field_display): ?>
            <th <?php if ($sort_by == $field_name)
                    echo "class=\"sort_$sort_order\"" ?>>
                <?php
                    echo anchor("films/display/$query_id/$field_name/" .
                            (($sort_order == 'asc' && $sort_by == $field_name) ? 'desc' : 'asc'),
                            $field_display);
                ?>
                    </th>
            <?php endforeach; ?>
                </thead>

                <tbody>
                    <?php foreach ($films as $film): ?>
                <tr>
                <?php foreach ($fields as $field_name => $field_display): ?>
                            <td>
            <?php echo $film->$field_name; ?>
                                </td>
<?php endforeach; ?>
                            </tr>
<?php endforeach; ?>
                        </tbody>

                    </table>

    <?php if (strlen($pagination)): ?>
                                <div>
                            		Pages: <?php echo $pagination; ?>
                                </div>
<?php endif; ?>
</body>
</html>

